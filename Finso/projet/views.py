# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render,redirect
from .form  import ProjetForm
from .models import Projet
from django.contrib.auth import authenticate, login, logout
from utilisateur.models import utilisateur

# Create your views here.

def projet(request):

    if request.method=="POST":
        form=ProjetForm(request.POST,request.FILES)
        if form.is_valid():
            ##categorie=Categorie.objects.filter(id=form.cleaned_data["categorie"])
            user=utilisateur.objects.get(pk=7)
            projet = Projet(nom=form.cleaned_data["nom"], description=form.cleaned_data["description"], Montant=form.cleaned_data["Montant"], id_user=user, date_debut=form.cleaned_data["Date_debut"], date_fin=form.cleaned_data["Date_fin"])
            projet.save()
            form=ProjetForm()
            handle_uploaded_file(request.FILES['file'])
            return render(request,'projet/projet.html',locals())
        else:
            form=ProjetForm()
            return render(request,'projet/projet.html',locals())
    else:
        form=ProjetForm()
        return render(request,'projet/projet.html',locals())


def handle_uploaded_file(f):
    with open('/Applications/Img/name.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

