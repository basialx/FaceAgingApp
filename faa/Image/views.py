import glob
import os

from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .form import ImageForm
from .models import Image
from django.http import HttpResponse
from .form import *
from .infer import make_image_older, display_image
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


@login_required(login_url='login')
# Create your views here.
def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            #zapytanie o ile lat?
        return redirect('image')
    else:
        form = ImageForm()
    return render(request, "index.html", {"form": form})

@login_required(login_url='login')
def image(request):
    if request.method == 'GET':
        latest_file = Image.objects.last()
        new1 = make_image_older(str(latest_file.image.path), 1)
        display_image(new1, str(latest_file.image.path))
        latest_file = Image.objects.all()
        return render(request, 'image.html', {'lf': latest_file})

#usuwanie zdjecia - to mozna dodac do galerii
@login_required(login_url='login')
def delete_image(request, id):
    image = Image.objects.get(pk=id)
    image.delete()
    return redirect('image')


======

def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Konto zostało stworzone jako ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, ' Niepoprawna nazwa użytkownika lub hasło')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
