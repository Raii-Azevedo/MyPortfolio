ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependências do MySQL client
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    MYSQLCLIENT_CFLAGS="-I/usr/include/mysql" \  # Verifique o caminho correto no seu sistema
    MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient" \  # Verifique o caminho correto no seu sistema
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

ENV SECRET_KEY "6PaBxqj2xoiEOcG5aCAvd5bPztF4QT8P388wAeoV7p8EW9lbYV"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "myport.wsgi"]
