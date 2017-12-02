from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projet.models import Projet 
from projet.models import Categorie
from projet.models import media
from projet.models import Projet_media
from django.contrib.auth.models import User


def home(request):
    projet=Projet.objects.filter(statut=0).select_related()
    categorie=Categorie.objects.all()
    liste_projet = []
    medi = []

    for i in projet:
        medi=media.objects.filter(id_projet=i.id).select_related()
        if len(medi)>0:
             proj=Projet_media(nom=i.nom, description=i.description, montant=i.Montant, url=medi[0].url)
             liste_projet.append(proj)

    return render(request, 'index.html', locals())


def projetbycategorie(request,id):
    categorie=Categorie.objects.all()
    projet=Projet.objects.filter(id_category=id)
    return render(request, 'projetcategorie/projet.html',locals())

def propos(request):
    categorie=Categorie.objects.all()
    return render(request, 'propos.html', locals())