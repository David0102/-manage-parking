from django.db import models
from cliente.models import Cliente

class Vaga(models.Model):
    numero = models.CharField('Número da vaga', max_length=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    disponivel = models.BooleanField('Disponível', default=True)

    def __str__(self):
        return self.numero