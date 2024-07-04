from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField
from django.db.models import CASCADE
from django.contrib.auth.models import User
class Contact(models.Model):
    nom1=models.CharField(max_length=255,blank=True)
    email1=models.EmailField(max_length=300,blank=True)
    sujet1=models.CharField(max_length=300,blank=True)
    message1=models.TextField(max_length=1000)

class Rdv(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="rdvs")
    nom2=models.CharField(max_length=255,blank=True)
    email2=models.EmailField(max_length=300,blank=True)
    tel=models.CharField(max_length=300,blank=True)
    date=models.DateField(max_length=1000,blank=True)
    message2=models.TextField(max_length=1000)

class Modifrdv(models.Model):
    nom3=models.CharField(max_length=255,blank=True)
    email3=models.EmailField(max_length=300,blank=True)
    tel1=models.CharField(max_length=300,blank=True)
    date1=models.DateField(max_length=1000,blank=True
    
    )
    message3=models.TextField(max_length=1000)

class Supprdv(models.Model):
    nom4=models.CharField(max_length=255)






# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = None

#     USERNAME_FIELD = 'email'
# Create your models here.
