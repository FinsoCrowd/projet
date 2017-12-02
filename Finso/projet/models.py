# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from utilisateur.models import utilisateur

# Create your models here.

class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    nom=models.CharField(max_length=255)
    description=models.TextField()

    class Meta:
        db_table = 'categorie'

class Projet(models.Model):
    id = models.AutoField(primary_key=True)
    nom=models.CharField(max_length=255)
    description=models.TextField()
    Montant=models.DecimalField(max_digits=19, decimal_places=2)
    statut=models.CharField(max_length=255,default=0)
    date_debut=models.DateField()
    date_fin=models.DateField()
    id_user = models.ForeignKey(utilisateur, db_column="id_user", on_delete=models.CASCADE)
    id_category=models.ForeignKey(Categorie,db_column="id_category", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'projet'



class media(models.Model):
    id = models.AutoField(primary_key=True)
    nom=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    url=models.CharField(max_length=255)
    id_projet = models.ForeignKey(Projet, db_column="id_projet", on_delete=models.CASCADE)

    class Meta:
        db_table = 'media'

class Projet_media(object):
    def __init__(self, nom, description, montant, url ):
        self.nom = nom
        self.description= description
        self.montant=montant
        self.url=url


