from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('images/', views.images, name='images'),
    path('<int:id>', views.delete_image, name='delete'),
    #path('result/', views.result, name='result'),
]