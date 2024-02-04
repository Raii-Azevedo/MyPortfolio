from django.contrib import admin
from .models import Home, About, Services, Experience, Portfolio, Jobs

# Register your models here.

admin.site.register(Home)
admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Jobs)
admin.site.register(Services)
admin.site.register(Portfolio)