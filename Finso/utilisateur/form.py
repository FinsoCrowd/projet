from django import forms

from .models import utilisateur

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

      class Meta:
            model = User
            fields=('username','email','password')

class UtilisateurForm(UserForm):
      
      class Meta(UserForm.Meta):
          model = utilisateur
          fields=('siteweb','adresse','tel','typ')



class ConnexionForm(forms.Form):
      username=forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
      password=forms.CharField(label="Mots de passe", max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control'}))