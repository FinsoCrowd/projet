# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.shortcuts import render,redirect
from .form import UserForm
from .form  import UtilisateurForm
from .form import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from .models import utilisateur


def register(request):

    if request.method=="POST":
        form=UserForm(request.POST)
        formU=UtilisateurForm(request.POST)
        if form.is_valid() and formU.is_valid() :
            usere = User.objects.create_user(form.cleaned_data["username"],form.cleaned_data["email"],form.cleaned_data["password"] )
            utilisateure = utilisateur(user=usere,adresse=formU.cleaned_data["adresse"], siteweb=formU.cleaned_data["siteweb"], typ=formU.cleaned_data["typ"], tel=formU.cleaned_data["tel"])
            utilisateure.save()
            form=UserForm()
            formU=UtilisateurForm()
            return render(request,'utilisateur/register.html',locals())
        else:
            form=UserForm()
            formU=UtilisateurForm()
            return render(request,'utilisateur/register.html',locals())
    else:
        form=UserForm()
        formU=UtilisateurForm()
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
               return render(request,'admin/admin1.html')
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



def update(request):
    if request.method=="POST":
        usere=utilisateur.objects.get(user=request.user)
        form=UserForm(request.POST, instance=request.user)
        formU=UtilisateurForm(request.POST, instance=usere )
        if form.is_valid() and formU.is_valid() :
            #usere = User.objects.create_user(form.cleaned_data["username"],form.cleaned_data["email"],form.cleaned_data["password"] )
            #utilisateure = utilisateur(user=usere,adresse=formU.cleaned_data["adresse"], siteweb=formU.cleaned_data["siteweb"], typ=formU.cleaned_data["typ"], tel=formU.cleaned_data["tel"])
            #utilisateure.save()
            #form=UserForm()
            #formU=UtilisateurForm()
            form.save()
            formU.save()
            form=UserForm()
            formU=UtilisateurForm()
            return render(request,'utilisateur/update.html',locals())
        else:
            form=UserForm()
            formU=UtilisateurForm()
            return render(request,'utilisateur/update.html',locals())


    
    else:
         usere=utilisateur.objects.get(user=request.user)
         print (usere.adresse)
         form=UserForm(request.POST or None,instance=request.user)
         formU=UtilisateurForm(request.POST or None,instance=usere)
         return render(request, 'utilisateur/update.html',locals())






# Create your views here.
