ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependências do MySQL client, pkg-config, gcc e dependências de compilação para Pillow e django-stdimage
RUN apt-get update && apt-get install -y \
    libpq-dev \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Instalar o django-stdimage
RUN pip install django-stdimage

COPY . /code

ENV SECRET_KEY "6PaBxqj2xoiEOcG5aCAvd5bPztF4QT8P388wAeoV7p8EW9lbYV"
# Executar a coleta estática após instalar o django-stdimage
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "myport.wsgi"]
