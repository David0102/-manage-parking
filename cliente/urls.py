from django.urls import path
from cliente import views

urlpatterns = [
    path('', views.index, name='clientes')
]
