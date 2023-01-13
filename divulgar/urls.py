from django.urls import path
from . import views

urlpatterns = [
    path('cadastroPet/', views.cadastroPet,name= "cadastroPet"),
    path('seus_pets/', views.seus_pets, name="seus_pets"),
    path('remover_pet/<int:id>', views.remover_pet, name="remover_pet"),
    path('ver_pet/<int:id>', views.ver_pet, name="ver_pet"),
]
   

