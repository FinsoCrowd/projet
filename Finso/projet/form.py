from django import forms

from .models import Projet
from .models import Categorie

class ProjetForm(forms.Form):

     CHOICES=[ (o.id, o.nom) for o in Categorie.objects.all()]
     nom=forms.CharField(label="Nom", max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':''})) 
     description=forms.CharField(label="Description", max_length=30, widget=forms.Textarea(attrs={'class':'form-control','placeholder':''}))
     Montant=forms.DecimalField(label="Montant", widget=forms.NumberInput(attrs={'class':'form-control','placeholder':''}))
     Date_debut=forms.DateField(label="Date debut", widget=forms.DateInput(attrs={'class':'form-control','placeholder':''}))
     Date_fin=forms.DateField(label="Date fin", widget=forms.DateInput(attrs={'class':'form-control','placeholder':''}))
     Categorie = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
     file=forms.FileField()

     