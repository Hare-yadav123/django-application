from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse,HttpResponseRedirect
from .forms  import SignForm
from.forms import LoginForm,ContactForm
from django.contrib.auth import authenticate
# Create your views here.

# class MyClass(View):
#     def get(self,request):
#         return render(request,'copper/home.html')

def home(request):
    return render(request,'copper/home.html')

def about(request):
    return render(request,'copper/about.html')

def service(request):
    return render(request,'copper/service.html')

def team(request):
    return render(request,'copper/team.html')

def blog(request):
    return render(request,'copper/blog.html')

def contact(request):
    return render(request,'copper/contact.html')

def page(request):
    return render(request,'copper/pages.html')


# SignUp Form

def signup(request):
    if request.method=='POST':
        fm=SignForm(request.POST)
        if fm.is_valid():
            fm.save()
            # HttpResponseRedirect('/login/')
            fm=SignForm()
    else:
        fm=SignForm()
    return render(request,'copper/signup.html',{'form':fm})

# Login Form

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            email=request.POST.get('email')
            password=request.POST.get('password')
            user=authenticate(username=email,password=password)
            if user is not None:
                LoginForm(request,user)
                return redirect('/home')
    else:
        form=AuthenticationForm()
    return render(request,'copper/login.html',{'form':form})


# contact Form

def contact(request):
    if request.method=='POST':
        fm=ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            # HttpResponseRedirect('/login/')
            fm=ContactForm()
    else:
        fm=ContactForm()
    return render(request,'copper/contact.html',{'form':fm})

