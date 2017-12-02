from django import forms

from .models import Contribution

class ContributionForm(forms.Form):
     
     CHOICES = (('1', 'Joni joni'),('2', 'Orange Money'),)
     commentaire=forms.CharField(label="Description", max_length=30, widget=forms.Textarea(attrs={'class':'form-control','placeholder':''}))
     Montant=forms.DecimalField(label="Montant", widget=forms.NumberInput(attrs={'class':'form-control','placeholder':''}))
     type_payement = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
     
