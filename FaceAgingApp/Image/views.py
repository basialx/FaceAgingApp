from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image
from django.http import HttpResponse
from .form import *
from . import infer
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
        i = Image.objects.get(id=1)
        infer.main()
        image = Image.objects.all()
        return render(request, 'images.html', {'image': image})


def delete_image(request, id):
    image = Image.objects.get(pk=id)
    image.delete()
    return redirect('images')
