from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image
from django.http import HttpResponse
from .form import *

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            #
        obj = form.instance
        #return render(request, "index.html", {"obj": obj})
        return redirect('success')
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "index.html", {"img": img, "form": form})


""" if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('success')
        obj = form.instance
        return render(request, "index.html", {"obj": obj})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "index.html", {"img": img, "form": form})
"""
def success(request):
    return HttpResponse('successfully uploaded')

# Python program to view
# for displaying images

def display_images(request):
	if request.method == 'GET':
		image = Image.objects.all()
		return render((request, 'images.html',
					{'images': image}))
