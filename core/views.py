from django.shortcuts import render
from .models import Post, About  

# Create your views here.
def index(request):
    abouts = About.objects.all()
    return render(request, 'index.html', {'about': abouts})

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'content': posts})