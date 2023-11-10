from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=12)
    data_nascimento = models.DateField('Data_Nascimento')
    telefone = models.CharField('Telefone', max_length=50)

    def __str__(self):
        return self.nome
