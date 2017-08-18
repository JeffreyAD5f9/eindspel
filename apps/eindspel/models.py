from __future__ import unicode_literals

from django.db import models
import re, bcrypt
#if bcrypt module is not recognized, djangoenv is not actvated

class userManager(models.Manager):
    def validUser(self, post):
        valid = True
        errors = []

        if len(post.get('userName')) == 0:
            errors.append('Username must not be empty.')
            valid = False
        if len(post.get('password')) == 0:
            errors.append('Password must not be empty.')
            valid = False
        if post.get('cpassword') != post.get('password'):
            errors.append('User Password and Confirmation do not Match.')
            valid = False
        return {"status" : valid, "Errors" : errors}


    def userCreate(self, post):
        return User.objects.create(
            userName = post.get('userName'),
            password = bcrypt.hashpw(post.get('password').encode(),bcrypt.gensalt()),
            collection = '[1, 1, 1, 1, 1, 2, 3, 4, 5]'
        )


    def checkUser(self, post):
        valid = True
        errors = []
        user = User.objects.filter(userName = post.get('logName')).first()

        if len(post.get('logName')) == 0:
            errors.append('Username must not be empty.')
            valid = False
        if len(post.get('logPassword')) == 0:
            errors.append('Enter Password.')
            valid = False
        if not user:
            errors.append('Username not found in Database.')
            valid = False
        if valid != False:
            if bcrypt.hashpw(post.get('logPassword').encode(), user.password.encode()) != user.password:
                errors.append('Username and Password do not Match.')
                valid = False
            else:
                return {'status': True, 'user': user}
        return {"status" : valid, "Errors" : errors}

class deckManager(models.Manager):
    def validDeck(self, post):
        valid = True
        errors = []

        if len(post.get('deckName')) == 0:
            errors.append('Deck Name must not be empty.')
            valid = False
        if len(post.get('points')) > 60:
            errors.append('Total value of pieces in deck exceeds 60pts.')
            valid = False

        return {"status" : valid, "Errors" : errors}

    def deckCreate(self, post, userCurrent):
        return Deck.objects.create(
            deckName = post.get('deckName'),
            points = post.get('points'),
            pieces = post.get('pieces'),
            owner = userCurrent
        )

    def searchDeck(self, post, userCurrent):
        valid = True
        errors = []

        if Deck.objects.filter(deckName = post.get('deckSelect')).first() not in Deck.objects.filter(owner = userCurrent):
            errors.append('Deck not found in your profile.')
            valid = False

        return {"status" : valid, "Errors" : errors}

    def locateDeck(self, post, userCurrent):
        return Deck.objects.get(deckName = post.get('deckSelect'))

class statPieceManager(models.Manager):
    def validPiece(self, post):
        valid = True
        errors = []

        if len(post.get('piecename')) == 0:
            errors.append('Piece Name must not be empty.')
            valid = False
        if len(post.get('identifier')) == 0:
            errors.append('Id Number must not be empty.')
            valid = False
        if len(post.get('health')) == 0:
            errors.append('Health must not be empty.')
            valid = False
        if len(post.get('attack')) == 0:
            errors.append('Attack must not be empty.')
            valid = False
        if len(post.get('defense')) == 0:
            errors.append('Defense must not be empty.')
            valid = False
        if len(post.get('atkRange')) == 0:
            errors.append('Attack Range must not be empty.')
            valid = False
        if len(post.get('movement')) == 0:
            errors.append('Movement must not be empty.')
            valid = False
        if len(post.get('abilities')) == 0:
            errors.append('Abilities Array must not be empty.')
            valid = False
        if len(post.get('placement')) == 0:
            errors.append('Placement Spaces must not be empty.')
            valid = False
        if len(post.get('deckVal')) == 0:
            errors.append('Deck Value must not be empty.')
            valid = False
        if len(post.get('graphic')) == 0:
            errors.append('Front Graphic must not be empty.')
            valid = False
        if len(post.get('graphicr')) == 0:
            errors.append('Back Graphic must not be empty.')
            valid = False

        return {"status" : valid, "Errors" : errors}

    def staticPieceCreate(self, post):
        return PieceStatic.objects.create(
            pieceName = post.get('piecename'),
            identifier = post.get('identifier'),
            health = post.get('health'),
            attack = post.get('attack'),
            defense = post.get('defense'),
            atkRange = post.get('atkRange'),
            movement = post.get('movement'),
            abilities = post.get('abilities'),
            placement = post.get('placement'),
            deckVal = post.get('deckVal'),
            graphic = post.get('graphic'),
            graphicR = post.get('graphicr')
        )


    def addPieceManual(self, post):
        valid = True
        errors = []

        if len(post.get('addition')) == 0:
            errors.append('Piece Number must not be empty.')
            valid = False

        return {"status" : valid, "Errors" : errors}

    def staticPieceUpdateManual(self, post):
        User.objects.filter(userName = 'Akural').update(collection = post.get('addition'))



#-----------------Models-------------------------

class User(models.Model):
    userName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    collection = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = userManager()

class Deck(models.Model):
    deckName = models.CharField(max_length=255)
    points = models.CharField(max_length=255)
    pieces = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name = "decksOwned")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = deckManager()

class PieceStatic(models.Model):
    pieceName = models.CharField(max_length=255)
    identifier = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    atkRange = models.IntegerField()
    movement = models.IntegerField()
    abilities = models.CharField(max_length=255) #abilities = an array of ability identifiers [1,A2,g10, ......]
    placement = models.CharField(max_length=255)
    deckVal = models.IntegerField()
    graphic = models.CharField(max_length=255)
    graphicR = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = statPieceManager()
