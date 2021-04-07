from django.shortcuts import render
from django.views import generic
from .forms import UserRegistrationForm, EditProfileForm, PasswordChangingForm, EditUserProfileForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import PasswordChangeView


# Create your views here.
# class UserRegistrationView(generic.CreateView):
#     form_class = UserRegistrationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class EditUserProfileView(generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = 'registration/edit_bio_and_pic.html'
    success_url = reverse_lazy('edit_profile')

    def get_object(self):
        try:
            return self.request.user.userprofile
        except:
            pass