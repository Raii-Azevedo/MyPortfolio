from django.db import models

# Create your models here.
class Base(models.Model):
    criado = models.DateTimeField("Criação", auto_now_add = True)
    modificado = models.DateTimeField("Atualização", auto_now = True)

    class Meta:
        abstract = True


class Home(Base):
    resume = models.TextField('Resumo')

    class Meta:
        verbose_name = "Home"

    def __str__(self):
        return self.resume
    

class About(Base):
    title = models.CharField("Cargo", max_length = 300)
    description = models.TextField("Descrição")

    class Meta:
        verbose_name = "About"

    def __str__(self):
        return self.title
    
class Experience(Base):
    education = models.CharField("Educação", max_length = 300)
    description = models.TextField("Descrição")
    period = models.CharField("Período", max_length = 300)

    class Meta:
        verbose_name = "Education"

    def __str__(self):
        return self.education
    
class Jobs(Base):
    cargo = models.CharField("Cargo", max_length = 300)
    company = models.CharField("Company", max_length = 300, default='Freelance')
    description = models.TextField("Descrição")
    period = models.CharField("Período", max_length = 300)

    class Meta:
        verbose_name = "Cargo"

    def __str__(self):
        return self.cargo
  
class Services(Base):
    service = models.CharField("Cargo", max_length = 300)
    description = models.TextField("Descrição")

    ICON_CHOICES = (
        ('bxs-dashboard', 'dashboard'),
        ('bx-line-chart', 'gráfico'),
        ('bx-code-alt', 'developer'),
    )

    icone = models.CharField('Icone', max_length=20, choices=ICON_CHOICES, default='bx-code-alt')

    class Meta:
        verbose_name = "Service"

    def __str__(self):
        return self.service
    
class Portfolio(models.Model):
    title = models.CharField("Projeto", max_length=300)
    description = models.CharField("Descrição", max_length=400)
    link = models.CharField("Link", max_length=300)
    image = models.ImageField("Imagem", upload_to='portfolio_images/', null=True, blank=True)

    class Meta:
        verbose_name = "Projeto"

    def __str__(self):
        return self.title
