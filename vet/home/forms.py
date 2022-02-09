from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import FileInput, TextInput
from django.urls import reverse

from home.models import Animal
from user.models import User

#Register Form
class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=30, label='User Name :')
    email = forms.EmailField(max_length=200, label='Email :')
    first_name = forms.CharField(max_length=100,  label='First Name :')
    last_name = forms.CharField(max_length=100, label='Last Name :')

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

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name','species','genus','age','description', 'image',]
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'name'}),
            'species': TextInput(attrs={'class': 'input', 'placeholder': 'species'}),
            'genus': TextInput(attrs={'class': 'input', 'placeholder': 'genus'}),
            'age': TextInput(attrs={'class': 'input', 'placeholder': 'age'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }





