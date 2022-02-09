from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

from home.forms import SignUpForm
from home.models import  Animal
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


#index page
from user.models import User


def index(request):
    animals = Animal.objects.all()
    users = User.objects.all()
    context = {
        'animals': animals,
        'users': users
    }

    return render(request, 'index.html', context)




#Register
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Hoş geldiniz... Sitemize başarılı bir şekilde üye oldunuz.")
            return HttpResponseRedirect('/')

    form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


#Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Hatalı Giriş! Kullanıcı adı ve ya şifre yanlış")
            return HttpResponseRedirect('/login')

    return render(request, 'login.html')

#Logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


#List Animals
def animals(request):
    animals = Animal.objects.all().order_by('?')
    context = {
        'animals':animals
    }
    return render(request, 'animals.html', context)