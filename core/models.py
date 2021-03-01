from django.db import models
from stdimage.models import StdImageField
import uuid


def _get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}, {ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Sobre(Base):
    imagem = StdImageField('Imagem', upload_to='about', variations={'thumb': {'width': 508, 'height': 550, 'crop': True}})
    descricao = models.TextField('Descrição', max_length=500, default='')
    nome = models.CharField('Nome', max_length=100)
    experiencia = models.CharField('Experiência', max_length=50)
    pais = models.CharField('País', max_length=30, default='Brasil')
    local = models.CharField('Endereço', max_length=100)
    email = models.EmailField('E-Mail', max_length=100)
    telefone = models.CharField('Número', max_length=20)
    freela = models.BooleanField('Disponível pra Freela?', default='Disponível')

    class Meta:
        verbose_name = 'sobre'
        verbose_name_plural = 'sobres'

    def __str__(self):
        return self.nome


class Servico(Base):
    ICONE_CHOICES = (
        ('icon-grid', 'quadrinhos'),
        ('icon-layers', 'design'),
        ('icon-bubbles', 'balões'),
        ('icon-briefcase', 'maleta'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.CharField('Descrição', max_length=300)
    icone = models.CharField('Icone', max_length=14, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'servico'
        verbose_name_plural = 'servicos'

    def __str__(self):
        return self.servico



