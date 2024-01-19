from django.urls import path
from faturamento.views import faturamentos


urlpatterns = [
    path('', faturamentos, name="faturamentos"),
]