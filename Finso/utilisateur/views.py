# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.shortcuts import render,redirect

from .form  import UtilisateurForm
from .form import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from .models import utilisateur


def register(request):

    if request.method=="POST":
        form=UtilisateurForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data["username"],form.cleaned_data["email"],form.cleaned_data["password"] )
            utilisateure = utilisateur(adresse=form.cleaned_data["adresse"], siteweb=form.cleaned_data["siteweb"], typ=form.cleaned_data["typ"], tel=form.cleaned_data["tel"])
            utilisateure.save()
            form=UtilisateurForm()
            return render(request,'utilisateur/register.html',locals())
        else:
            form=UtilisateurForm()
            return render(request,'utilisateur/register.html',locals())
    else:
        form=UtilisateurForm()
        return render(request,'utilisateur/register.html',locals())
 

def connexion (request):
    error=False
    if request.method=="POST":
        form=ConnexionForm(request.POST)
        if form.is_valid():
             username=form.cleaned_data["username"]
             password=form.cleaned_data["password"]
             user=authenticate(username=username,password=password)
             if user:
               login(request,user)
               return render(request,'index.html')
             else:
                error=True
                form=ConnexionForm()
                return render(request,'utilisateur/login.html',locals())
    else:
        form=ConnexionForm()
        return render(request,'utilisateur/login.html',locals())


def deconnexion (request):
    logout(request)
    return redirect('/utilisateur/connexion')

# Create your views here.
