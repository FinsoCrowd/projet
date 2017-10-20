from django import forms

from .models import Projet

class ProjetForm(forms.Form):
     
     CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
     nom=forms.CharField(label="Nom", max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':''})) 
     description=forms.CharField(label="Description", max_length=30, widget=forms.Textarea(attrs={'class':'form-control','placeholder':''}))
     Montant=forms.DecimalField(label="Montant", widget=forms.NumberInput(attrs={'class':'form-control','placeholder':''}))
     Date_debut=forms.DateField(label="Date debut", widget=forms.DateInput())
     Date_fin=forms.DateField(label="Date fin", widget=forms.DateInput(attrs={'class':'form-control','placeholder':''}))
     Categorie = forms.ChoiceField(choices=CHOICES)
     file=forms.FileField()

     