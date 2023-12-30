# Use a imagem oficial do Python
ARG PYTHON_VERSION=3.10-slim-bullseye
FROM python:${PYTHON_VERSION}

# Configurações do Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalação de dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Criação e configuração do diretório de trabalho
RUN mkdir -p /code
WORKDIR /code

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt /tmp/requirements.txt

# Instalação das dependências do projeto
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Copia o código-fonte para o contêiner
COPY . /code

# Configuração do segredo da aplicação (não use um valor fixo em produção)
ENV SECRET_KEY "6PaBxqj2xoiEOcG5aCAvd5bPztF4QT8P388wAeoV7p8EW9lbYV"

# Executa as migrações do Django
RUN python manage.py migrate

# Executa a coleta estática
RUN python manage.py collectstatic --noinput

# Exposição da porta
EXPOSE 8000

# Comando para iniciar o servidor Gunicorn
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "myport.wsgi"]
