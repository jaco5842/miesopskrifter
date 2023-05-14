from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.opskrifter, name='home'),
    path('opskrifter/', views.opskrifter, name='opskrifter'),
    path('ny-opskrift/', views.ny_opskrift, name='ny-opskrift'),
    path('admin/', admin.site.urls, name='admin'),
    path('update_recipe/', views.update_recipe_tested, name='mark_recipe_tested'),
    path('delete_recipe/', views.mark_recipe_deleted, name='mark_recipe_tested'),
    path('slettede_opskrifter/', views.slettede_opskrifter, name='slettede_opskrifter'),
    
]
