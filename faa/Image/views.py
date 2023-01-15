import glob
import os

from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image
from django.http import HttpResponse
from .form import *
import torch
import sys
from .infer import make_image_older
sys.path.insert(0, '/engine')
# Create your views here.
def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

        """obj = form.instance
        obj.detected_img = infer.main()
        print(obj.detected_img)"""
        # return render(request, "index.html", {"obj": obj})
        return redirect('images')
    else:
        form = ImageForm()
    return render(request, "index.html", {"form": form})


def images(request):
    if request.method == 'GET':
        #list_of_files = glob.glob('C:/Users/patkr/faa/media/*.jpg')  # * means all if need specific format then *.csv
        latest_file = Image.objects.last()
        new = make_image_older(latest_file, 1)
        new.save()
        image = Image.objects.all()
        return render(request, 'image.html', {'image': image, 'lf':new})


def delete_image(request, id):
    image = Image.objects.get(pk=id)
    image.delete()
    return redirect('images')
