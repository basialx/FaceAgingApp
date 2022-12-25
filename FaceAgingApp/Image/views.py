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
        return redirect('images')
    else:
        form = ImageForm()
    return render(request, "index.html", {"form": form})

def images(request):
	if request.method == 'GET':
		image = Image.objects.all()
		return render(request, 'images.html',{'image': image})

def delete_image(request, id):
    image = Image.objects.get(pk=id)
    image.delete()
    return redirect('images')