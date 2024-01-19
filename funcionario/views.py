from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.urls import reverse

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
        senha2 = request.POST.get('senha2')

        if senha != senha2:
            messages.error(request, "As senhas devem ser iguais!")
            return redirect('cadastrar_funcionario')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "O email fornecido já pertence a um funcionário cadastrado!")
            return redirect('cadastrar_funcionario')
            
        try:
            user = User.objects.create_user(username=usuario, password=senha, email=email, first_name=nome)
            if user:
                messages.success(request, "Funcionário cadastrado com sucesso!")
                return redirect('funcionarios')
        
        except IntegrityError:
            messages.error(request, "O nome de usuário fornecido já pertence a um funcionário cadastrado!")
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

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Funcionário deletado com sucesso!')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Funcionário deletado com sucesso!')
        return super().get_success_url()
    
@login_required
def change_password_get(request, id):
    return render(request, "funcionario/atualizar_senha.html", {"id_user":id})
    
def change_password_post(request):
    id_user = request.POST.get("id_user")
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    senha3 = request.POST.get('senha3')

    user = User.objects.get(id=id_user)

    senha_hash = user.password

    if check_password(senha, senha_hash):
        if senha2 == senha3:
            if check_password(senha2, senha_hash):
                messages.error(request, "A nova senha não pode ser igual a senha atual!")
                return redirect(reverse('change_password_get', kwargs={"id":id_user}))
            else:
                user.set_password(senha2)
                user.save()
                messages.success(request, "Senha alterada com sucesso!")
                return redirect('funcionarios')
        else:
            messages.error(request, "As senhas devem ser iguais!")
            return redirect(reverse('change_password_get', kwargs={"id":id_user}))
    
    messages.error(request, "A senha atual fornecida está incorreta!")
    return redirect(reverse('change_password_get', kwargs={"id":id_user}))

def busca_funcionario(request):
    username = request.POST.get('username')

    try:
        funcionario = User.objects.exclude(is_superuser=True).get(username=username)
        return render(request, 'funcionario/busca_funcionario.html', {'funcionario':funcionario})
    
    except User.DoesNotExist:
        messages.error(request, "Não existe um funcionário com o username informado!")
        return redirect('funcionarios')