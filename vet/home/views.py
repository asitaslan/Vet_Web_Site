from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

from home.forms import SignUpForm, AnimalForm
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


#add Animal
@login_required(login_url='/login')
def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Animal()
            data.owner_id = current_user.id
            data.name = form.cleaned_data['name']
            data.species = form.cleaned_data['species']
            data.genus = form.cleaned_data['genus']
            data.age = form.cleaned_data['age']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.save()
            messages.success(request, 'Ekleme basarili')
            return HttpResponseRedirect('/user')
        else:
            messages.success(request, 'Content Form Error:' + str(form.errors))
            return HttpResponseRedirect('/add_animal')
    else:

        form = AnimalForm()
        context = {

            'form': form,

        }
        return render(request, 'add_animals.html', context)


#animal detail
@login_required(login_url='/login')
def animal_detail(request, id):
    animal = Animal.objects.get(id=id)
    context = {

        'animal':animal
    }
    return  render(request, 'animal_detail.html', context)

#Edit Animal
@login_required(login_url='/login')
def update_animal(request, id):
    animal = Animal.objects.get(id=id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guncelleme Basarili')
            return HttpResponseRedirect('/user')
        else:
            messages.success(request, 'animal Form Error: ' + str(form.errors))
            return HttpResponseRedirect('/update_animal/' + str(id))
    else:

        form = AnimalForm(instance=animal)
        context = {
            'form': form,
        }
        return render(request, 'update_animal.html', context)


# delete animal
@login_required(login_url='/login')
def delete_animal(request, id):
    current_user = request.user
    if current_user.is_superuser:
        Animal.objects.filter(id=id).delete()
        messages.success(request, 'Hayvan Silindi')
        return HttpResponseRedirect('/animals')
    else:
        messages.error(request,'Bu islemi yapma yetkiniz yok')
        return HttpResponseRedirect('/animals')