from django.urls import path
from .views import index, blog

urlpatterns = [
    path('', index, name='index'),
    path('blog.html', blog, name='blog')
    ]