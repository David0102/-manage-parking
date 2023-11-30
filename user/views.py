from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'user/login.html'

    def form_valid(self, form):
        messages.success(self.request, "Login efetuado com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Credenciais inválidas. Tente novamente!")
        return super().form_invalid(form)

@login_required
def painel(request):
    return render(request, 'user/painel.html')

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "Logout realizado com sucesso!")
        return super().dispatch(request, *args, **kwargs)