from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User


def login(request):
    form = LoginForms()

    return render(request, "usuarios/login.html", {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha'].value() != form['senha_confirmar'].value():
                return redirect('cadastro')

            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha'].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('login')

    return render(request, "usuarios/cadastro.html", {"form": form})


# def logout(request):
#     pass
