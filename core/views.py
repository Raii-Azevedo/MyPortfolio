from django.shortcuts import render
from .models import Home, About, Experience, Portfolio, Services, Jobs
from django.http import HttpResponse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.parser import BytesParser
from email.policy import default
import os



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


def receber_email(request):
    if request.method == 'POST':
        # Verificar se o cabeçalho Content-Type é application/json
        content_type = request.headers.get('Content-Type', '')
        if 'application/json' not in content_type:
            return HttpResponse("Only JSON content type is supported", status=415)

        try:
            # Analisar o corpo da solicitação JSON para obter o e-mail
            data = BytesParser(policy=default).parsebytes(request.body)
            email_body = data.get_payload()
            sender_email = data['From']

            # Configurações de e-mail do Gmail
            EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
            EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

            # Criar mensagem de e-mail
            msg = MIMEMultipart()
            msg['From'] = gmail_user
            msg['To'] = 'destinatario@gmail.com'  # E-mail do destinatário no Gmail
            msg['Subject'] = 'Assunto do e-mail'

            # Corpo do e-mail
            body = email_body
            msg.attach(MIMEText(body, 'plain'))

            # Conectar-se ao servidor SMTP do Gmail
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_password)

            # Enviar e-mail
            text = msg.as_string()
            server.sendmail(gmail_user, 'destinatario@gmail.com', text)
            server.quit()

            return HttpResponse("E-mail enviado com sucesso!", status=200)
        except Exception as e:
            return HttpResponse("Erro ao processar o e-mail: " + str(e), status=500)
    else:
        return HttpResponse(status=405)