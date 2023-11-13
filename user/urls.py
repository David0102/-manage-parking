from django.urls import path
from django.contrib.auth.views import LogoutView
from user import views

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('painel/', views.painel, name='painel'),
]
