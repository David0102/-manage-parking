from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, "Login efetuado com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Credenciais inválidas. Tente novamente!")
        return super().form_invalid(form)

@login_required
def painel(request):
    return render(request, 'painel.html')