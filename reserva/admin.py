from django.contrib import admin
from reserva.models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'vaga', 'horario_entrada', 'horario_saida', 'valor', 'status')
