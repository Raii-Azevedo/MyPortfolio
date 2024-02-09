from django.urls import path
from .views import index, enviar_email

urlpatterns = [
    path('', index, name='index'),
    path('enviar_email/', enviar_email, name='enviar_email'),
    ] 