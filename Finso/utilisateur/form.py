from django import forms

from .models import utilisateur

class UtilisateurForm(forms.ModelForm):
      
      class Meta:
          model = utilisateur
          fields=('username','email','password','siteweb','adresse','tel','typ')
      


class ConnexionForm(forms.Form):
      username=forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
      password=forms.CharField(label="Mots de passe", max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control'}))