from django.urls import path
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('about', views.about, name='about'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', views.LikeView, name='like_post')
]