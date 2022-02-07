from django.shortcuts import render, redirect
from home.forms import SignUpForm, UserUpdateForm
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from home.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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

#Update User
@login_required(login_url='/login')  # Check login
def user_update(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)  # request.user is user data
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
@login_required(login_url='/login')  # Check login
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
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