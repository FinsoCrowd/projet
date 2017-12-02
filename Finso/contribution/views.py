# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .form import ContributionForm
from projet.models import Projet, Categorie
from .models import  Contribution

from django.contrib.auth import authenticate, login, logout
from utilisateur.models import utilisateur
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def contributeprojet(request,id):
    categorie=Categorie.objects.all()
    user=utilisateur.objects.get(user=request.user)
    if request.method=="POST":
        form=ContributionForm(request.POST)
        if form.is_valid():
            projet=Projet.objects.get(pk=id)
            user=utilisateur.objects.get(user=request.user)
            contribution=Contribution(id_user=user, id_projet=projet, commentaire=form.cleaned_data["commentaire"], montant=form.cleaned_data["Montant"], Date=date.today(), Type_payement=form.cleaned_data["type_payement"] )
            contribution.save()
            form=ContributionForm()
            return render(request, 'contribution/contribution.html',locals())
    else:
        form=ContributionForm()
        return render(request, 'contribution/contribution.html',locals())


