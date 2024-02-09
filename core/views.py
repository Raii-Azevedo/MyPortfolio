from django.shortcuts import render
from .models import Home, About, Experience, Portfolio, Services, Jobs
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.core.mail import send_mail


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


def enviar_email(request):
    # Lógica para processar os dados do formulário e enviar o e-mail
    if request.method == 'POST':
        # Obtenha os dados do formulário
        full_name = request.POST.get('full_name')
        email_address = request.POST.get('email_address')
        mobile_number = request.POST.get('mobile_number')
        email_subject = request.POST.get('email_subject')
        message = request.POST.get('message')

        # Construa o corpo do e-mail
        email_body = f"""
        Nome: {full_name}
        E-mail: {email_address}
        Número de telefone: {mobile_number}
        
        Mensagem:
        {message}
        """

        # Envie o e-mail
        send_mail(
            email_subject,
            email_body,
            email_address,  # Deve ser o e-mail do remetente
            ['rhaii.azevedo@gmail.com'],  # Lista de destinatários
            fail_silently=False,
        )

        # Obtendo o token CSRF
        csrf_token = get_token(request)
        
        # Criando a resposta HTTP
        response = HttpResponse("E-mail enviado com sucesso!")
        
        # Definindo o cookie com SameSite=None e o token CSRF como valor
        response.set_cookie('XSRF-TOKEN', csrf_token, samesite='None')
        
        return response
    else:
        # Retorna uma resposta de erro se o método da solicitação não for POST
        return HttpResponse("Método de solicitação inválido!")