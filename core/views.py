from django.shortcuts import render
from .models import Home, About, Experience, Portfolio, Services, Jobs
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
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
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email_address = request.POST.get('email_address')
        mobile_number = request.POST.get('mobile_number')
        email_subject = request.POST.get('email_subject')
        message = request.POST.get('message')

        # Construa o conteúdo do e-mail
        email_content = f"Nome: {full_name}\nE-mail: {email_address}\nNúmero de telefone: {mobile_number}\nAssunto: {email_subject}\nMensagem: {message}"

        # Envie o e-mail
        send_mail(
            subject='Novo contato do formulário de contato',
            message=email_content,
            from_email=email_address,
            recipient_list=['rhaii.azevedo@gmail.com'],
            fail_silently=False,
        )

        # Retorne uma resposta ao cliente
        return HttpResponse("O e-mail foi enviado com sucesso!")
    else:
        # Se a solicitação não for POST, retorne uma resposta de método não permitido
        return HttpResponse("Método não permitido.", status=405)