from django.contrib import admin
from .models import Sobre, Servico


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('nome','imagem', 'descricao', 'experiencia', 'pais', 'local', 'email', 'telefone', 'freela')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'descricao')

