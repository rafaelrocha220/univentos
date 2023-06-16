from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from datetime import date, time
import random
from .models import Produtor, Eventos


def home(request):
    return render(request, 'home.html', {})


def login(request):
    return render(request, 'login.html', {})


@csrf_exempt
def loginPost(request):
    user = Produtor.objects.filter(username=request.POST.get(
        'username'), password=request.POST.get('password'))

    if user.exists():
        # Autenticação bem-sucedida
        print("Usuário autenticado:", user)
        # Armazenar os dados na sessão
        request.session['usuario'] = user[0].username
        return redirect('eventos')

    else:
        # Credenciais inválidas
        print("Credenciais inválidas")
        return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html', {})


@csrf_exempt
def registerPost(request):
    if request.method == 'POST':
        user = Produtor(username=request.POST.get('username'),
                        password=request.POST.get('password'))
        user.save()
    return redirect('login')


def eventos_cadastrar(request):
    return render(request, 'evento_cadastrar.html', {})


def eventos_editar(request):
    ultimo_evento = Eventos.objects.latest('id')
    return render(request, 'evento_editar.html', {'evento': ultimo_evento})


@csrf_exempt
def evento_cadastrar_post(request):
    evento = Eventos(
        nome='Meu Evento',
        tipo_evento='Conferência',
        data_inicio=date.today(),
        hora_inicio=time(9, 0),
        hora_fim=time(18, 0),
        endereco='Rua Principal, 123',
        cidade='Minha Cidade',
        estado='Meu Estado',
        qtd_ingresso=str(random.randint(1, 500)),
        valor_ingresso='50.00',
        taxa_univentos=False
    )
    evento.save()

    return redirect('eventos')


def eventos_list(request):
    username = request.session['usuario'] if request.session.get(
        'usuario') is not None else False
    return render(request, 'meus_eventos.html', {'username': username, 'eventos': Eventos.objects.all()})


def evento_read(request):
    ultimo_evento = Eventos.objects.latest('id')
    return render(request, 'evento.html', {'evento': ultimo_evento})


def evento_delete(request):
    ultimo_evento = Eventos.objects.latest('id')
    ultimo_evento.delete()
    return redirect('eventos')
