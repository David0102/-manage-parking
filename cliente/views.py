from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from cliente.models import Cliente
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    context_object_name = 'clientes'
    template_name = 'cliente/clientes.html'

@login_required
def cadastrar_cliente(request):
    if request.method == 'GET':
        return render(request, 'cliente/cadastrar_cliente.html')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        telefone = request.POST.get('telefone')

        if Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "O CPF já está vinculado a um cliente!")
            return redirect('cadastrar_cliente')
        
        elif Cliente.objects.filter(telefone=telefone).exists():
            messages.error(request, "O telefone já está vinculado a um cliente!")
            return redirect('cadastrar_cliente')
            
        else:
            cliente = Cliente(
                nome = nome,
                cpf = cpf,
                data_nascimento = data_nascimento,
                telefone = telefone
            )

            cliente.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('clientes')

@login_required
def editar_cliente_get(request, pk):
    cliente = Cliente.objects.get(id=pk)
    return render(request, 'cliente/editar_cliente.html', {'cliente': cliente})


def editar_cliente_post(request):
        cliente_id = request.POST.get('cliente_id')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        telefone = request.POST.get('telefone')

        if Cliente.objects.filter(cpf=cpf).exclude(id=cliente_id).exists():
            messages.error(request, "O CPF já está vinculado a um cliente!")
            return redirect(reverse('editar_cliente_get', kwargs={'pk':cliente_id}))
        
        elif Cliente.objects.filter(telefone=telefone).exclude(id=cliente_id).exists():
            messages.error(request, "O telefone já está vinculado a um cliente!")
            return redirect(reverse('editar_cliente_get', kwargs={'pk':cliente_id}))
        
        else:
            cliente = Cliente.objects.get(id=cliente_id)
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.data_nascimento = data_nascimento
            cliente.telefone = telefone
            cliente.save()

            messages.success(request, "Cliente atualizado com sucesso!") 
            return redirect('clientes')


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/deletar_cliente.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('clientes')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Cliente deletado com sucesso!')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Cliente deletado com sucesso!')
        return super().get_success_url()


def busca_cliente(request):
    cpf = request.POST.get('cpf')

    try:
        cliente = Cliente.objects.get(cpf=cpf)
        return render(request, 'cliente/cliente_busca.html', {'cliente':cliente})
    
    except Cliente.DoesNotExist:
        messages.error(request, "Não existe um cliente com o CPF informado!")
        return redirect('clientes')