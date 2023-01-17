from django.urls import path
from . import views

urlpatterns = [
    path('listar_pets/', views.listar_pets, name="listar_pets"),
    path('pedido_adocao/<int:id_pet>',views.pedido_adocao ,name= "pedido_adocao"),
    path('ver_pedido_adocao/', views.ver_pedido_adocao, name="ver_pedido_adocao"),
]
