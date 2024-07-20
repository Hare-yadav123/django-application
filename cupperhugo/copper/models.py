from django.db import models

# Create your models here.
class SignUpModel(models.Model):
    First_Name= models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Phone_No=models.BigIntegerField()
    Password=models.CharField(max_length=100)
    Conform_password=models.CharField(max_length=100,default=40)

class Login(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class ContactModel(models.Model):
    your_name=models.CharField(max_length=100)
    working_mail=models.EmailField(max_length=100)
    company_website=models.CharField(max_length=100)
    feed_back=models.CharField(max_length=100)
