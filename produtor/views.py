from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})

# Login requisition get


def login(request):
    return render(request, 'login.html', {})

# Register requistion get


def register(request):
    return render(request, 'register.html', {})


def eventos_cadastrar(request):

    return render(request, 'evento_cadastrar.html', {})
