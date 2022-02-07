from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, FileInput, EmailInput

from home.models import User

#Register Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name :')
    email = forms.EmailField(max_length=200, label='Email :')
    first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name :')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name :')

    class Meta:
        model = User
        fields = (
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2',
                  )

#Update User Form
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('profile_image','username','email','first_name','last_name','phone', 'adress')
        widgets = {
            'profile_image': FileInput(attrs={'class': 'input', 'placeholder': 'profile_image'}),
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'adress': TextInput(attrs={'class': 'input', 'placeholder': 'adress'}),
        }