# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class utilisateur(User):
    adresse=models.CharField(max_length=255)
    siteweb=models.CharField(max_length=255)
    typ=models.CharField(max_length=255)
    tel=models.CharField(max_length=255)

