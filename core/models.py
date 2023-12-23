import uuid
from django.db import models
from stdimage.models import StdImageField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User



def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()},{ext}'
    return filename

# Create your models here.
class Base(models.Model):
    criados = models.DateTimeField('Criação', auto_now_add=True)
    modificado = models.DateTimeField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Documento(Base):
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return f'Documento {self.id}'
    
    
class About(Base):
    about = models.CharField('About', max_length=200)
    description = models.TextField('Description', max_length= 300)
   
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.about
    
    
class Service (Base):
    service = models.CharField('Service', max_length = 200)
    service_desc = models.TextField('Description', max_length = 300)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Projects (Base):
    project = models.CharField('Project Name', max_length = 200)
    project_desc = models.TextField('Project', max_length = 300)
    proj_img = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project
    
# BLOG
class Post(models.Model):
    title = models.CharField(max_length = 255)
    resume = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    youtube_url = models.URLField(blank=True, null=True, verbose_name='YouTube URL')

    def __str__(self):
        return self.title
