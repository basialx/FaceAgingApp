import glob
import os

from django.shortcuts import render, redirect

from .form import ImageForm
from .models import Image
from django.http import HttpResponse
from .form import *
import torch
from .infer import make_image_older, display_image

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# Create your views here.
def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('images')
    else:
        form = ImageForm()
    return render(request, "index.html", {"form": form})


def images(request):
    if request.method == 'GET':
        latest_file = Image.objects.last()
        new = make_image_older(str(latest_file.image.path), 3)
        display_image(new, str(latest_file.image.path))
        latest_file = Image.objects.last()
        image = Image.objects.all()
        return render(request, 'image.html', {'image': image, 'lf': latest_file})


def delete_image(request, id):
    image = Image.objects.get(pk=id)
    image.delete()
    return redirect('images')

#def redirect_to_index(request):
#    return redirect('index')
