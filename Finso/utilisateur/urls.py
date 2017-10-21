from django.conf.urls import url
from django.contrib import admin
from . import views


app_name='utilisateur'
urlpatterns = [
    url(r'^register/', views.register, name="register"),
    url(r'^connexion/', views.connexion, name="connexion"),
    url(r'^deconnexion/', views.deconnexion, name="deconnexion"),
    url(r'^modifier/', views.update, name="modifier"),
]