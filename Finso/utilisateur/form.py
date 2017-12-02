from django import forms

from .models import utilisateur

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

      class Meta:
            model = User
            fields=('username','email','password')
            widgets = {
                 'username': forms.TextInput(attrs={'class':'form-control'}),
                 'email': forms.TextInput(attrs={'class':'form-control'}),
                 'password': forms.PasswordInput(attrs={'class':'form-control'}),
             }
            labels = {
                  'username': ('Identifiant'),
             }    

class UtilisateurForm(UserForm):
      
      class Meta(UserForm.Meta): 
          model = utilisateur
          fields=('siteweb','adresse','tel','typ')
          widgets = {
                 'siteweb': forms.TextInput(attrs={'class':'form-control'}),
                 'adresse': forms.TextInput(attrs={'class':'form-control'}),
                 'tel': forms.PasswordInput(attrs={'class':'form-control'}),
                 'typ': forms.Select(attrs={'class':'form-control'})
             }
          labels ={
                 'tel': ('Telephone'),
                 'typ':('Type'),
                 'siteweb': ('Site-Web'),
          }
            



class ConnexionForm(forms.Form):
      username=forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
      password=forms.CharField(label="Mots de passe", max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}))