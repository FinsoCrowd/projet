from django.conf.urls import url
from django.contrib import admin
from . import views

app_name='administration'
urlpatterns = [
    url(r'^home', views.home, name='admin1'),
    url(r'^detail/(?P<id>\d+)', views.detail, name='detail'),
    url(r'^detail1/(?P<id>\d+)', views.detail1, name='detail1'),
    url(r'^modifier/(?P<id>\d+)', views.modifier, name='modifier'),
    url(r'^supprimer/(?P<id>\d+)', views.supprimer, name='supprimer'),
    url(r'^valider', views.valider, name='valider'),
    url(r'^categorie', views.categorie, name='categorie'),
    url(r'^supp/(?P<id>\d+)', views.supp, name='supp'),
    url(r'^mod/(?P<id>\d+)', views.mod, name='mod'),
]