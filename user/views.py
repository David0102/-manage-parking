from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('painel')
        else:
            return redirect('login')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def painel(request):
    return render(request, 'painel.html')