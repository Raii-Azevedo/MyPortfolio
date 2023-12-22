from django.contrib import admin
from core.models import Documento, About, Service, Projects, Post

# Register your models here.

admin.site.register(About)
admin.site.register(Documento)
admin.site.register(Service)
admin.site.register(Projects)
admin.site.register(Post)