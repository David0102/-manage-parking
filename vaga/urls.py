from django.urls import path
from vaga.views import VagaListView

urlpatterns = [
    path('', VagaListView.as_view(), name='vagas'),
]
