from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('image/', views.image, name='image'),
    path('<int:id>', views.delete_image, name='delete'),
]