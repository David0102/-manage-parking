from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib import messages

@login_required
def funcionarios(request):
    funcionarios_objects = User.objects.exclude(is_superuser=True)
    return render(request, 'funcionario/funcionarios.html', {'funcionarios': funcionarios_objects})

@login_required
def cadastrar_funcionario(request):
    if request.method == 'GET':
        return render(request, 'funcionario/cadastrar_funcionario.html')
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            user = User.objects.create_user(username=usuario, password=senha, email=email, first_name=nome)
            if user:
                messages.success(request, "Funcionário cadastrado com sucesso!")
                return redirect('funcionarios')
        
        except IntegrityError:
            messages.error(request, "Nome de usuário já existe!")
            return redirect('cadastrar_funcionario')

@login_required
def editar_funcionario_get(request, pk):
    funcionario = User.objects.get(id=pk)
    return render(request, 'funcionario/editar_funcionario.html', {'funcionario': funcionario})


def editar_funcionario_post(request):
        funcionario_id = request.POST.get('funcionario_id')
        nome = request.POST.get('nome')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')

        if User.objects.filter(username=usuario).exclude(id=funcionario_id).exists():
            messages.error(request, "Nome de usuário já existe!")
            return redirect('funcionarios')
        
        else:
            funcionario = User.objects.get(id=funcionario_id)
            funcionario.first_name = nome
            funcionario.username = usuario
            funcionario.email = email
            funcionario.save()

            messages.success(request, "Funcionário atualizado com sucesso!")
            return redirect('funcionarios')

class FuncionarioDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'funcionario/deletar_funcionario.html'
    context_object_name = 'funcionario'
    success_url = reverse_lazy('funcionarios')