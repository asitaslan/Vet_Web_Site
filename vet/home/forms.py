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


#Animal form
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name','species','genus','age','description', 'image',]
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'isim'}),
            'species': TextInput(attrs={'class': 'input', 'placeholder': 'tür'}),
            'genus': TextInput(attrs={'class': 'input', 'placeholder': 'cins'}),
            'age': TextInput(attrs={'class': 'input', 'placeholder': 'yaş'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'açıklama'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'resim', }),
        }



#Search form
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

