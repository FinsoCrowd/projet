# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from utilisateur.models import utilisateur
from projet.models import Projet

# Create your models here.

class Contribution(models.Model):
    CHOICES = (('1', 'Joni joni'),('2', 'Orange Money'),)  
    id = models.AutoField(primary_key=True)
    commentaire = models.CharField(max_length=30)
    id_user = models.ForeignKey(utilisateur, db_column="id_user", on_delete=models.CASCADE)
    id_projet = models.ForeignKey(Projet, db_column="id_projet", on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=17, decimal_places=13)
    Date = models.DateField()
    Type_payement = models.CharField(choices= CHOICES, default="1",  max_length=255)

    class meta:
        db_table = 'contribution'

