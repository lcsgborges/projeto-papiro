from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

            usuario = auth.authenticate(request,
            username=username,
            password=password)

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{username}autenticado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('login')
    else:
        form = LoginForms()
        return render(request, 'usuarios/login.html', {"form":form})


def cadastro(request):
    if request.method == 'GET':
        form = CadastroForms()
        return render(request, 'usuarios/cadastro.html', {"form":form})
    else:
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form['password'].value() != form['password2'].value():
                messages.error(request, 'As senhas precisam ser iguais')
                return redirect('cadastro')

            nome = form['nome'].value()
            username = form['username'].value()
            email = form['email'].value()
            password = form['password'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Esse usuário já existe')
                return redirect('cadastro')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Esse email já foi utilizado')
                return redirect('cadastro')
            

            nome = nome.split()
            if nome[0] == nome[-1]:
                messages.error(request, 'Informe seu nome completo')
                return redirect('cadastro')
            
            username = username.strip()
            if " " in username:
                messages.error(request, 'Não pode haver espaços no seu nome de usuário')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=username,
                email=email,
                first_name=nome[0],
                last_name=nome[-1],
                password=password,
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('login')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Você foi desconectado.')
    return redirect('index')


def index(request):
    return render(request, 'index.html')