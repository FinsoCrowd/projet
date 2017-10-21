from django import forms

from projet.models import Categorie


class CategorieForm(forms.Form):
	nom=forms.CharField(label="Nom", max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nom'}))
	description=forms.CharField(label="Description", max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}))