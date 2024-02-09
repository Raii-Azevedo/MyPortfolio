from django.shortcuts import render
from .models import Home, About, Experience, Portfolio, Services, Jobs
from django.http import HttpResponse
from django.middleware.csrf import get_token


def index(request):
    home = Home.objects.all()
    about = About.objects.all()
    experience = Experience.objects.all()
    portfolio = Portfolio.objects.all()
    services = Services.objects.all()
    jobs = Jobs.objects.all()  # Adicionando esta linha

    context = {
        'home': home,
        'about': about,
        'experience': experience,
        'jobs': jobs,  # Corrigindo o nome da chave e associando o valor
        'portfolio': portfolio,
        'services': services,
    }

    return render(request, 'index.html', context)


def minha_view(request):
    # Obtendo o token CSRF
    csrf_token = get_token(request)
    
    # Criando a resposta HTTP
    response = HttpResponse("Hello, world!")
    
    # Definindo o cookie com SameSite=None e o token CSRF como valor
    response.set_cookie('XSRF-TOKEN', csrf_token, samesite='None')
    
    return response