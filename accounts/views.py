from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request,"accounts/home.html")

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"you are registered successfully.Please login")
            return redirect("login")
        else:
            print(form.errors)
    else:
        form=RegisterForm()
    
    return render(request,"accounts/register.html",{"form":form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request,f"Welcome Back,{user.username}!")
            return redirect("dashboard")
    else:
        form=AuthenticationForm()
    return render(request,"accounts/login.html",{"form":form})

@login_required
def dashboard(request):
    return render(request,"accounts/dashboard.html")

def logout_view(request):
    logout(request)
    messages.success(request,"you have been successfully logged out")
    return redirect("home")

