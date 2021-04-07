from django.urls import path
from .views import UserEditView, PasswordChangeView, EditUserProfileView
from . import views

urlpatterns = [
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('edit_user_profile/', EditUserProfileView.as_view(), name='edit_user_profile'),
    path('register/', views.register, name='register'),
    path('password/', PasswordChangeView.as_view(template_name='registration/change-password.html'), name='change_password')
]