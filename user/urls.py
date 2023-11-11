from django.urls import path
from user import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('painel/', views.painel, name='painel'),
]
