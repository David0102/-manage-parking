from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    cpf = models.CharField('CPF', max_length=12)
    data_nascimento = models.DateField('Data_Nacimento', blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=50)

    def __str__(self):
        return self.username