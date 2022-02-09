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
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'adress': TextInput(attrs={'class': 'input', 'placeholder': 'adress'}),
        }