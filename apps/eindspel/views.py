from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import *

def userInit(request):
    if 'userCurrent' in request.session:
        return User.objects.get(id = request.session['userCurrent'])


def index(request):

  return render(request, 'eindspel/index.html')

def start1(request):
    if request.method != 'POST':
        return redirect('/')
    test = Deck.objects.searchDeck(request.POST, userInit(request))

    if test['status'] == True:
        user = userInit(request)
        deckLocated = Deck.objects.locateDeck(request.POST, userInit(request))
        deckPieces = []
        for element in deckLocated.pieces:
            if element.isdigit():
                piece = PieceStatic.objects.get(identifier = element)
                deckPieces.append(piece)
        print deckPieces
        context = {
            'userCurrent': user,
            'activeDeck': deckPieces
        }
        return render(request, 'eindspel/field1.html', context)
    else:
        for error in test['Errors']:
            messages.add_message(request, messages.ERROR, error, extra_tags="decks")
        return redirect('/')





def genesis(request):

  return render(request, 'eindspel/genesis.html')


def register(request):
    if request.method != 'POST':
        return redirect('/')
    test = User.objects.validUser(request.POST)

    if test['status'] == True:
        user = User.objects.userCreate(request.POST)
        request.session['userCurrent'] = user.id
        return redirect('/gotoDeckManager')
    else:
        for error in test['Errors']:
            messages.add_message(request, messages.ERROR, error, extra_tags="register")
        return redirect('/')

def generator(request):
    if request.method != 'POST':
        return redirect('/genesis')
    test = PieceStatic.objects.validPiece(request.POST)

    if test['status'] == True:
        user = PieceStatic.objects.staticPieceCreate(request.POST)
        return redirect('/gotoDeckManager')
    else:
        for error in test['Errors']:
            messages.add_message(request, messages.ERROR, error, extra_tags="register")
        return redirect('/genesis')


def access(request):
    if request.method != 'POST':
        return redirect('/genesis')
    test = PieceStatic.objects.addPieceManual(request.POST)

    if test['status'] == True:
        PieceStatic.objects.staticPieceUpdateManual(request.POST)
        return redirect('/gotoDeckManager')
    else:
        for error in test['Errors']:
            messages.add_message(request, messages.ERROR, error, extra_tags="access")
        return redirect('/genesis')


def gotoDeckManager(request):
    user = userInit(request)
    decks = user.decksOwned.all()
    staticIds = []
    pieces = PieceStatic.objects.all()
    userCollection = []
    for piece in pieces:
        staticIds.append(str(piece.identifier))
    for element in user.collection:
        if element in staticIds:
            userCollection.append(pieces.get(identifier = element))

    context = {
        'userCurrent': user,
        'decks': decks,
        'userCollection' : userCollection
    }

    return render(request, 'eindspel/deckManager.html', context)


def deckBuilder(request):
    if request.method != 'POST':
        return redirect('/')
    test = Deck.objects.validDeck(request.POST)

    if test['status'] == True:
        deck = Deck.objects.deckCreate(request.POST, userInit(request))
        return redirect('/gotoDeckManager')
    else:
        for error in test['Errors']:
            messages.add_message(request, messages.ERROR, error, extra_tags="deckReg")
        return redirect('/')


def login(request):
    if request.method != 'POST':
        return redirect('/')
    test = User.objects.checkUser(request.POST)
    if test['status'] == True:
        request.session['userCurrent'] = test['user'].id
        return redirect('/gotoDeckManager')
    else:
        for error in test['Errors']:
		    messages.add_message(request, messages.ERROR, error, extra_tags="login")
        return redirect('/')



def logout(request):
    request.session.clear()

    return redirect('/')
