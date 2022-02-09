from django import forms
from django.forms import TextInput, FileInput, EmailInput
from user.models import User


#Update User Form
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('profile_image','username','email','first_name','last_name','phone', 'adress')
        widgets = {
            'profile_image': FileInput(attrs={'class': 'input'}),
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'kullanici adi'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'ad'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'soyad'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'telefon'}),
            'adress': TextInput(attrs={'class': 'input', 'placeholder': 'adres'}),
        }