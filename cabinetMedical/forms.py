from typing import Any
from django import forms
from cabinetMedical.models import Contact,Rdv,Modifrdv,Supprdv
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Inscription(UserCreationForm):
    username=forms.CharField(label='Nom d utilisateur',widget=forms.TextInput(attrs={'placeholder': 'Votre nom d utilisateur', 'style': 'margin-top:20px;margin-bottom:20;', 'class': 'form-control'}))
    first_name=forms.CharField(label='Nom',widget=forms.TextInput(attrs={'placeholder': 'Votre nom', 'style': 'margin-top:20px;margin-bottom:20;', 'class': 'form-control'}))
    last_name=forms.CharField(label='Prenom',widget=forms.TextInput(attrs={'placeholder': 'Votre prenom', 'style': 'margin-top:20px;margin-bottom:20', 'class': 'form-control'}))
    class Meta(UserCreationForm.Meta):
        model=get_user_model()
        fields=['username','email','first_name','last_name']
    def __init__(self, *args ,**kwargs):
        super(Inscription,self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'

    

class Connexion(forms.Form):
    nom=forms.CharField(label='Votre nom',widget=forms.TextInput(attrs={'placeholder': 'Votre nom', 'style': 'margin-top:20px;margin-bottom:20;', 'class': 'form-control'}))
    motDePasse=forms.CharField(label='Mot de passe',widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe', 'style': 'margin-top:20px;margin-bottom:20;', 'class': 'form-control'}))


class ContactForm(forms.ModelForm):
   class Meta:
     model = Contact
     fields = '__all__'
     labels={
        "nom1":"Votre nom",
        "email1":"Votre email",
        "sujet1":"Votre sujet",
        "message1":"votre message",
     }
   #   nom1=forms.CharField(required=False)
     widgets={
        'nom1':forms.TextInput(attrs={ "required":False ,'style': 'width:700px;height:50px;', 'class': 'form-control'}),
        'email1':forms.EmailInput(attrs={ "required":False ,'style': 'width:700px;height:50px;', 'class': 'form-control'}),
        'sujet1':forms.TextInput(attrs={ "required":False ,'style': 'width:700px;height:50px;', 'class': 'form-control'}),
        'message1':forms.TextInput(attrs={ 'style': 'width:700px;height:200px;', 'class': 'form-control'}),
     }
   #  "required":False ,

class RdvForm(forms.ModelForm):
   class Meta:
     model = Rdv
     fields = ["nom2", "email2", "tel", "date","message2"]
     labels={
        "nom2":"Votre nom",
        "email2":"Votre email",
        "tel":"Votre tel",
        "date":"La date du rdv",
        "message2":"votre message",
     }
     widgets={
        'nom2':forms.TextInput(attrs={ "required":False,'style': 'width:700px;height:50px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
        'email2':forms.EmailInput(attrs={ "required":False,'style': 'width:700px;height:50px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
        'tel':forms.NumberInput(attrs={"required":False, 'style': 'width:700px;height:50px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
        'date':forms.DateInput(attrs={ "required":False,'style': 'width:700px;height:50px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
        'message2':forms.TextInput(attrs={ 'style': 'width:700px;height:200px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
     }


class ModifrdvForm(forms.ModelForm):
   class Meta:
     model = Modifrdv
     fields = '__all__'
     labels={
        "nom3":"Votre nom",
        "email3":"Votre email",
        "tel1":"Votre tel",
        "date1":"La date du rdv",
        "message3":"votre message",
     }
     widgets={
        'nom3':forms.TextInput(attrs={ "required":False,'style': 'width:700px;height:50px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
        'email3':forms.EmailInput(attrs={ "required":False,'style': 'width:700px;height:50px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
        'tel1':forms.NumberInput(attrs={ "required":False,'style': 'width:700px;height:50px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
        'date1':forms.DateInput(attrs={ "required":False,'style': 'width:700px;height:50px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
        'message3':forms.TextInput(attrs={ 'style': 'width:700px;height:200px;margin-left: auto;margin-right: auto;', 'class': 'form-control'}),
     }


class SupprdvForm(forms.ModelForm):
   class Meta:
     model = Supprdv
     fields = '__all__'
     labels={
        "nom4":"Votre nom",
     }
     widgets={
        'nom4':forms.TextInput(attrs={ 'style': 'height:50px;width: 50vw; margin-left : 10vw;', 'class': 'form-control'}),
     }


# nom=forms.CharField(label='Votre nom',widget=forms.TextInput(attrs={'placeholder': 'Votre nom', 'style': 'margin-top:20px;margin-bottom:20;', 'class': 'form-control'}))
    # motDePasse=forms.CharField(label='Mot de passe',widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe', 'style': 'margin-top:20px;margin-bottom:20;', 'class': 'form-control'}))
    # CmotDePasse=forms.CharField(label='Confirmer le mot de passe',widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe', 'style': 'margin-top:20px;margin-bottom:20', 'class': 'form-control'}))
    # def clean(self):
    #     cleaned_data=self.cleaned_data
    #     motDePasse=self.cleaned_data.get("motDePasse")
    #     CmotDePasse=self.cleaned_data.get("CmotDePasse")
    #     if motDePasse != CmotDePasse:
    #         raise forms.ValidationError("Les mots de passe doivent etre identique.")
    #     return cleaned_data







    
