# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from projet.models import Projet,Categorie,media
from django.contrib.auth.models import User
from .form  import CategorieForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def detail(request,id):
	user=request.user
	projet=Projet.objects.get(id=id)
	m=media.objects.filter(id_projet=id)
	return render(request, 'admin/detail.html',locals())
# Create your views here.
@login_required
def detail1(request,id):
	user=request.user
	projet=Projet.objects.get(id=id)
	m=media.objects.filter(id_projet=id)
	return render(request, 'admin/detail1.html',locals())
@login_required
def home(request):
	user=request.user
	projet=Projet.objects.filter(statut=0).select_related()
	#user = User.objects.create_user('abdoul', 'lennon@thebeatles.com', 'passer')
	return render(request, 'admin/admin1.html',locals())
@login_required
def modifier(request,id):
	user=request.user
	Projet.objects.filter(pk=id).update(statut=1)
	projet=Projet.objects.filter(statut=0).select_related()
	return redirect('/admin1/home')
@login_required
def supprimer(request,id):
	user=request.user
	projet=Projet.objects.get(pk=id).delete()
	#user = User.objects.create_user('abdoul', 'lennon@thebeatles.com', 'passer')
	return redirect('/admin1/home')
@login_required
def valider(request):
	user=request.user
	projet=Projet.objects.filter(statut=1).select_related()
	#user = User.objects.create_user('abdoul', 'lennon@thebeatles.com', 'passer')
	return render(request, 'admin/valider.html',locals())
@login_required
def categorie(request):

    if request.method=="POST":
        form=CategorieForm(request.POST)
        user=request.user
        if form.is_valid():
            
            categorie = Categorie(nom=form.cleaned_data["nom"],description=form.cleaned_data["description"])
            categorie.save()
            form=CategorieForm()
            return render(request,'admin/categorie.html',locals())
        else:
            form=CategorieForm()
            return render(request,'admin/categorie.html',locals())
    else:
        form=CategorieForm()
        user=request.user
        return render(request,'admin/categorie.html',locals())