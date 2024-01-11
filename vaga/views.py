from django.shortcuts import render
from vaga.models import Vaga
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class VagaListView(LoginRequiredMixin ,ListView):
    model = Vaga
    context_object_name = 'vagas'
    template_name = 'vaga/vagas.html'