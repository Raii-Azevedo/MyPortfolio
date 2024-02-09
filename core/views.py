from django.shortcuts import render
from .models import Home, About, Experience, Portfolio, Services, Jobs
from django.http import HttpResponse




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
    response = HttpResponse("Hello, world!")
    
    # Definindo o cookie com SameSite=None
    response.set_cookie('XSRF-TOKEN', 'valor_do_cookie', samesite='None')

    return response