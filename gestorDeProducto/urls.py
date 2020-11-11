from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('in', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('sucursal', views.sucursal, name='sucursal'),
    path('producto', views.producto, name='producto'),
   

#Forma de entrar a las paginas designadas

    # 127.0.0.1:8000/index
    # 127.0.0.1:8000/in
    # 127.0.0.1:8000/registro
    # 127.0.0.1:8000/sucursal
]