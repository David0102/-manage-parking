from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from cliente.models import Cliente
from django.contrib.auth.decorators import login_required

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    context_object_name = 'clientes'
    template_name = 'clientes.html'

@login_required
def cadastrar_cliente(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_cliente.html')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        telefone = request.POST.get('telefone')

        if Cliente.objects.filter(cpf=cpf).exists():
            return HttpResponse('CPF já está vinculado a um cliente.')
        
        elif Cliente.objects.filter(telefone=telefone).exists():
            return HttpResponse('Telefone já está vinculado a um cliente.')
        
        else:
            cliente = Cliente(
                nome = nome,
                cpf = cpf,
                data_nascimento = data_nascimento,
                telefone = telefone
            )

            cliente.save()

            return redirect('clientes')

@login_required
def editar_cliente_get(request, pk):
    cliente = Cliente.objects.get(id=pk)
    return render(request, 'editar_cliente.html', {'cliente': cliente})


def editar_cliente_post(request):
        cliente_id = request.POST.get('cliente_id')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        telefone = request.POST.get('telefone')

        if Cliente.objects.filter(cpf=cpf).exclude(id=cliente_id).exists():
            return HttpResponse('CPF já está vinculado a um cliente.')
        
        elif Cliente.objects.filter(telefone=telefone).exclude(id=cliente_id).exists():
            return HttpResponse('Telefone já está vinculado a um cliente.')
        
        else:
            cliente = Cliente.objects.get(id=cliente_id)
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.data_nascimento = data_nascimento
            cliente.telefone = telefone
            cliente.save()

            return redirect('clientes')


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'deletar_cliente.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('clientes')