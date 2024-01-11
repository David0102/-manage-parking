from django.db import models
from cliente.models import Cliente
from vaga.models import Vaga
from datetime import datetime

class Reserva(models.Model):
    
    STATUS_RESERVA = [
        ('em_andamento', 'Em andamento'),
        ('finalizada', 'Finalizada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    horario_entrada = models.DateTimeField('Horário de entrada')
    horario_saida = models.DateTimeField('Horário de saída', null=True, blank=True)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2, default=0.00)
    status = models.CharField('Status', max_length=20, choices=STATUS_RESERVA, default='em_andamento')

    def calcula_valor(self):
        duracao_reserva = (self.horario_saida - self.horario_entrada).total_seconds() / 60
        valor_reserva = duracao_reserva * 0.50

        self.valor = round(valor_reserva, 2)

        self.save()

    def __str__(self):
        return self.cliente.nome
