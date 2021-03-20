from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def about(request):
    return render(request, 'about.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'