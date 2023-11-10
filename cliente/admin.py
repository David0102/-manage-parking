from django.contrib import admin
from cliente.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento', 'telefone',)
