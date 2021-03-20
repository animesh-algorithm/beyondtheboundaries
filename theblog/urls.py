from django.urls import path
from .views import HomeView, ArticleView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('about', views.about, name='about')
]