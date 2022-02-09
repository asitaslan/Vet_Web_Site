from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Animal
from django.contrib.auth.decorators import login_required
from user.forms import UserUpdateForm
from user.models import User

#User Profile
@login_required(login_url='/login')  # Check login
def user_profile(request):
    current_user = request.user
    user_animals = Animal.objects.filter(owner_id=current_user.id)
    context = {
        'current_user':current_user,
        'user_animals':user_animals
    }
    return render(request, 'user_profile.html', context)


#Goto user detail
@login_required(login_url='/login')
def user_detail(request, id):
    user = User.objects.get(id=id)
    user_animals = Animal.objects.filter(owner_id=id)
    context = {
        'user':user,
        'user_animals':user_animals
    }
    return  render(request, 'user_detail.html', context)

#Update User
@login_required(login_url='/login')
def user_update(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)  # request.user is user data
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profiliniz Guncellendi')
            return redirect('/user')
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        'user_form': user_form
    }
    return render(request, 'update_user.html', context)


#Change password
@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sifreniz basarili bir sekilde degistirildi')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Lutfen sifreyi asagidaki kriterlere gore olusturunuz.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        form = PasswordChangeForm(request.user)
        context = {
            'form':form
        }
        return render(request, 'change_password.html', context)


#Users
def users(request):
    users = User.objects.all().order_by('?')
    context = {
        'users':users
    }
    return render(request, 'users.html', context)


