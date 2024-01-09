import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
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

    class Meta:
        abstract = True

class Documento(Base):
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return f'Documento {self.id}'

class Home(Base):

    short = models.CharField('Descrição', max_length=300)

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'

    def __str__(self):
        return self.short

    
class About(Base):
    about = models.CharField('Cargo', max_length=200, blank=True)
    description = models.TextField('Description', blank=True)
    college = models.CharField('College', max_length = 200)
    year = models.CharField('Year', max_length = 30)
    class_description = models.TextField('Job', max_length = 500)

    company = models.CharField('Company', max_length = 200 )
    job_year = models.CharField('Year', max_length = 30)
    job_description = models.TextField('Job', max_length = 500)

   
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.about
    
    
class Service (Base):
    ICON_CHOICES = (
        ('bx-code-alt', 'Web' ),
        ('bx-line-chart', 'Análise'),
        ('bxs-dashboard', 'Dashboard'),
    )
    icone = models.CharField('Icone', max_length=15, choices=ICON_CHOICES)
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
    
    proj_img = ProcessedImageField(upload_to=get_file_path,
                                   processors=[ResizeToFill(480, 480)],
                                   format='PNG',
                                   options={'quality': 90},
                                   verbose_name='Imagem')
   
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
