from django import forms
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('caption','image')


class CreateUserForm(UserCreationForm):
    class Meta:
        models = User
        fields = ['username', 'email', 'password1', 'password2']
