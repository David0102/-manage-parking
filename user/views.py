from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from cliente.models import Cliente
from django.contrib.auth.models import User
from vaga.models import Vaga
from reserva.models import Reserva
from datetime import datetime
from django.db.models import Sum


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
    clientes = Cliente.objects.all()
    funcionarios = User.objects.exclude(is_superuser = True)
    vagas = Vaga.objects.filter(disponivel=True)
    reservas = Reserva.objects.filter(status='em_andamento')
    total_vagas_dispo = len(vagas)
    total_reservas_em_andamento = len(reservas)
    total_funcionarios = len(funcionarios)
    total_clientes = len(clientes)

    data_hoje = datetime.now().date()
    reservas_diarias = Reserva.objects.filter(horario_entrada__date=data_hoje, 
        horario_saida__date=data_hoje, status='finalizada')
    faturamento_diario = reservas_diarias.aggregate(Sum('valor'))['valor__sum'] or 0

    return render(request, 'user/painel.html', {"total_clientes": total_clientes, 
    "total_funcionarios": total_funcionarios, "total_vagas":total_vagas_dispo, 
    "total_reservas":total_reservas_em_andamento, "Faturamento_diario":faturamento_diario})

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "Logout realizado com sucesso!")
        return super().dispatch(request, *args, **kwargs)