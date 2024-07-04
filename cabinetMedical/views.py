from django import forms
from django.shortcuts import render,redirect
from cabinetMedical.forms import Inscription,Connexion
from django.contrib.auth import authenticate,login
from django.conf import settings
from cabinetMedical.forms import ContactForm,RdvForm,ModifrdvForm,SupprdvForm
from django.contrib.auth.models import User
from cabinetMedical.models import Modifrdv,Supprdv,Rdv


# from django.http import HttpResponse
# Create your views here.

def cab(request):
    form=Inscription()
    form2=Connexion()
    form3=ContactForm()
    form4=RdvForm()
    form5=ModifrdvForm()
    form6=SupprdvForm()
    x=0
    # if request.user.is_authenticated:
    #     x=1
    nom5= 'xxx'
    # user1=User()
    message = ''
    if request.method == 'POST':
        form2 = Connexion(request.POST)
        if form2.is_valid():
            user = authenticate(
                username=form2.cleaned_data['nom'],
                password=form2.cleaned_data['motDePasse'],
            )
            if user is not None:
                login(request, user)
                x=1
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
            
        form = Inscription(request.POST)
        if form.is_valid():
            form.save()		
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)	
            x=1
            message = f'Bonjour, {user.username}! Vous êtes connecté.'
            return redirect('/cabinetMedical/cab')
         
        form3=ContactForm(request.POST)
        if form3.is_valid():
            form3.save()
            x=1
            return redirect('/cabinetMedical/cab')
        form4=RdvForm(request.POST)
        if form4.is_valid():
            nom=form4.cleaned_data['nom2']
            email=form4.cleaned_data['email2']
            tel1=form4.cleaned_data['tel']
            date1=form4.cleaned_data['date']
            message=form4.cleaned_data['message2']
            rdv=Rdv(user=request.user,nom2=nom,email2=email,tel=tel1,date=date1,message2=message)
            rdv.save()
            x=1
            return redirect('/cabinetMedical/cab')
        form5=ModifrdvForm(request.POST)
        if form5.is_valid():
            nom=form5.cleaned_data['nom3']
            email=form5.cleaned_data['email3']
            tel1=form5.cleaned_data['tel1']
            date1=form5.cleaned_data['date1']
            message=form5.cleaned_data['message3']
            up=Rdv.objects.get(user=request.user)
            up.delete()
            b=Rdv(user=request.user,nom2=nom,email2=email,tel=tel1,date=date1,message2=message)
            b.save()
            x=1
            return redirect('/cabinetMedical/cab')
        form6=SupprdvForm(request.POST)
        if form6.is_valid():
            nom=form6.cleaned_data['nom4']
            delet=Rdv.objects.get(user=request.user)
            delet.delete()
            x=1
            return redirect('/cabinetMedical/cab')

    contexte={
          "form":form,
          "form2":form2,
          "form3":form3,
          "form4":form4,
          "form5":form5,
          "form6":form6,
          "message":message,
          "x":x,
          "nom5":nom5,
        #   "user1":user1,
        
    }
    return render(request,'index.html',contexte)
    #  return render(request,'index.html',{}) 
    # user=form.save()
    


    # if form.is_valid():
    #         form.save()		
    #         username = form.cleaned_data.get('nom')
    #         password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=password)
    #         login(request,user)	
    #         return redirect(settings.LOGIN_REDIRECT_URL)



