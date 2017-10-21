# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from projet.models import Projet
from django.contrib.auth.models import User

# Create your views here.

def detail(request,id):
	projet=Projet.objects.get(id=id)
	return render(request, 'admin/detail.html',locals())

def home(request):
	projet=Projet.objects.filter(statut=0).select_related()
	#user = User.objects.create_user('abdoul', 'lennon@thebeatles.com', 'passer')
	return render(request, 'admin/admin1.html',locals())
def modifier(request,id):
	Projet.objects.filter(pk=id).update(statut=1)
	projet=Projet.objects.filter(statut=0).select_related()
	return redirect('/admin1/home')
def supprimer(request,id):
	projet=Projet.objects.get(pk=id).delete()
	#user = User.objects.create_user('abdoul', 'lennon@thebeatles.com', 'passer')
	return redirect('/admin1/home')
def valider(request):
	projet=Projet.objects.filter(statut=1).select_related()
	#user = User.objects.create_user('abdoul', 'lennon@thebeatles.com', 'passer')
	return render(request, 'admin/valider.html',locals())