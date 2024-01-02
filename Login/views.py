from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


def  index(request):
    return render(request, 'index.html')


def  register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        
    else:
        form = Register()
    return render(request, 'register.html', {'form':form})

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        
    else:
        form = AuthenticationForm()
    print(form)
    return render(request, 'login.html', {'form':form} )




def salir(request):
    logout(request)
    return redirect('index')