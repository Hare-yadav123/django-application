from django import forms
from. models import SignUpModel
from.models import Login,ContactModel

# Sifn Up form

class SignForm(forms.ModelForm):
    class Meta:
        # Password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
        # password2=forms.CharField(label='Conform Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
        model=SignUpModel
        fields=['First_Name','Last_Name','Email','Phone_No','Password','Conform_password']
        labels={'First_Name':'First Name','Last_Name':'Last Name','first_Name':'email','Email':'Email','Password':'Password'}
        widgets={
            'First_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Last_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Phone_No':forms.NumberInput(attrs={'class':'form-control'}),
            'Password':forms.PasswordInput(attrs={'class':'form-control'}),
            'Conform_password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

# Login form

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email','password']
        labels={'email':'Email','password':'Password'}
        widgets={
            'Email':forms.EmailInput(attrs={'autofuoc':True, 'class':'form-control'}),
            'Password':forms.PasswordInput(attrs={'autofuoc':True, 'class':'form-control'})
        }

# contact Form

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactModel
        fields=['your_name','working_mail','company_website','feed_back']
        labels={'your_name':'Your Name','working_mail':'Working Mail','company_website':'Company Website','feed_back':'Feed Back'}
        widgets={
            'your_name':forms.TextInput(attrs={'class':'form-control'}),
            'workin_mail':forms.EmailInput(attrs={'class':'form-control'}),
            'company_website':forms.TextInput(attrs={'class':'form-control'}),
            'feed_back':forms.TextInput(attrs={'class':'form-control'}),
        }
