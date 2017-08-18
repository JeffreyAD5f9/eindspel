from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^register$', views.register),
url(r'^genesis$', views.genesis),
url(r'^generator$', views.generator),
url(r'^deckBuilder$', views.deckBuilder),
url(r'^access$', views.access),
url(r'^gotoDeckManager$', views.gotoDeckManager),
url(r'^login$', views.login),
url(r'^logout$', views.logout),
url(r'^start1$', views.start1)

]
