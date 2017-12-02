# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class utilisateur(models.Model):
    CHOICES = (('Association', 'Association'),('Particulier', 'Particulier'),)  
    user=models.OneToOneField(User,unique="true")
    adresse=models.CharField(max_length=255)
    siteweb=models.CharField(max_length=255)
    typ=models.CharField(choices=CHOICES, default='Association', max_length=255)
    tel=models.CharField(max_length=255)

