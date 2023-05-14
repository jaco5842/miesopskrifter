from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

from . import views

def home(request):
    return HttpResponse ('Home page')


urlpatterns = [
    path('', views.opskrifter, name='home'),
    path('opskrifter/', views.opskrifter, name='opskrifter'),
    path('ny-opskrift/', views.ny_opskrift, name='ny-opskrift'),
    path('update_recipe/', views.update_recipe, name='update_recipe'),


]




