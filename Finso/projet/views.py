# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render,redirect
from .form  import ProjetForm
from .models import Projet
from .models import Categorie
from .models import media
from django.contrib.auth import authenticate, login, logout
from utilisateur.models import utilisateur
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def projet(request):
    categorie=Categorie.objects.all()
    if request.method=="POST":
        form=ProjetForm(request.POST,request.FILES)
        if form.is_valid():
            categorie=Categorie.objects.filter(id=form.cleaned_data["Categorie"])
            ##user = request.user
            categ= form.cleaned_data["Categorie"]
            print(categ)
            user=utilisateur.objects.get(user=request.user)
            projet = Projet(nom=form.cleaned_data["nom"], description=form.cleaned_data["description"], Montant=form.cleaned_data["Montant"], id_user=user, date_debut=form.cleaned_data["Date_debut"], date_fin=form.cleaned_data["Date_fin"], id_category=categorie[0])
            projet.save()
            #form=ProjetForm()
            numbmedia=media.objects.all().count()
            numbmedia+=numbmedia
            imgname="/Applications/media/image"+ str(numbmedia)+".png"
            nom="http://127.0.0.1:8083/media/image"+ str(numbmedia)+".png"
            medi = media(type='image',nom=nom, url=imgname, id_projet=projet)
            medi.save()

            handle_uploaded_file(request.FILES['file'], imgname)
            form=ProjetForm()
            return render(request,'projet/projet.html',locals())
        else:
            form=ProjetForm()
            return render(request,'projet/projet.html',locals())
    else:
        form=ProjetForm()
        return render(request,'projet/projet.html',locals())


def handle_uploaded_file(f,no):
    with open(no, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

