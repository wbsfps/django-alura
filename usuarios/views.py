from django.shortcuts import render, get_object_or_404


def login(request):
    return render(request, "usuarios/login.html")


def cadastro(request):
    return render(request, "usuarios/cadastro.html")


# def logout(request):
#     pass
