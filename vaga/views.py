from django.shortcuts import render, redirect
from vaga.models import Vaga
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class VagaListView(LoginRequiredMixin ,ListView):
    model = Vaga
    context_object_name = 'vagas'
    template_name = 'vaga/vagas.html'

def cadastrar_vaga(request):
    if request.method == 'GET':
        return render(request, 'vaga/cadastrar_vaga.html')
    
    if request.method == 'POST':
        num_vaga = request.POST.get('num_vaga')

        try:
            vaga = Vaga.objects.get(numero=num_vaga)
            messages.error(request, 'Vaga já cadastrada!')
            return redirect('cadastrar_vaga')

        except Vaga.DoesNotExist:
            vaga = Vaga(numero=num_vaga)
            vaga.save()
            messages.success(request, 'Vaga cadastrada com sucesso!')
            return redirect('vagas')

def confirm_delete_vaga(request, id):
    vaga = Vaga.objects.get(id=id)
    return render(request, 'vaga/deletar_vaga.html', {'vaga': vaga})

def deletar_vaga(request):
        id_vaga = request.POST.get('id_vaga')
        vaga = Vaga.objects.get(id=id_vaga)
        vaga.delete()
        messages.success(request, 'Vaga deletada com sucesso!')
        return redirect('vagas')