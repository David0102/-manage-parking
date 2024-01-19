from django.shortcuts import render
from datetime import datetime, timedelta
from reserva.models import Reserva
from django.db.models import Sum

def faturamentos(request):
    data_hoje = datetime.now().date()
    reservas_diarias = Reserva.objects.filter(horario_entrada__date=data_hoje, 
        horario_saida__date=data_hoje, status='finalizada')
    faturamento_diario = reservas_diarias.aggregate(Sum('valor'))['valor__sum'] or 0

    data_inicio_semana = data_hoje - timedelta(days=data_hoje.weekday())
    reservas_semanais = Reserva.objects.filter(horario_entrada__date__range=[data_inicio_semana, data_hoje], 
        horario_saida__date__range=[data_inicio_semana ,data_hoje], status='finalizada')
    faturamento_semanal = reservas_semanais.aggregate(Sum('valor'))['valor__sum'] or 0
    
    return render(request, "faturamento/faturamentos.html", {'faturamento_diario':faturamento_diario, 
        'faturamento_semanal':faturamento_semanal})
