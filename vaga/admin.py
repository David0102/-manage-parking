from django.contrib import admin
from vaga.models import Vaga

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cliente', 'disponivel')