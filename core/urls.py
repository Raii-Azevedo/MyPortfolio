from django.urls import path
from .views import index, blog, about_view

urlpatterns = [
    path('', index, name='index'),
    path('blog.html', blog, name='blog'),
    path('aboutC.html', about_view, name='about')
    ]