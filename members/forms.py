from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from theblog.models import UserProfile

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User

        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': ''
        }

        help_texts = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': ''
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'Last Name'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'Username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'Email Address'
                }
            )
        }
    
    def __init__(self, *args, **kwargs):

        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['password1'].widget.attrs['style'] = 'font-size: 20px;'
        self.fields['password2'].widget.attrs['style'] = 'font-size: 20px;'

        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password'

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username Already Taken')
        return self.cleaned_data

class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User

        fields = ('first_name', 'last_name', 'email', 'username')

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': ''
        }

        help_texts = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': ''
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'Last Name'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'Username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'Email Address'
                }
            )
        }

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     username = self.cleaned_data.get('username')
    #     if email != self.user.email:
    #         if User.objects.filter(email=email).exists():
    #             raise ValidationError('Email Already Exists')
    #     if username != self.user.username:
    #         if User.objects.filter(username=username).exists():
    #             raise ValidationError('Username Already Taken')
    #     return self.cleaned_data

class EditUserProfileForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_pic', 'user')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'id': 'bio', 'placeholder': 'Type your content here....', 'style': 'display:none'})
        }

class PasswordChangingForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):

        super(PasswordChangingForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].label = ''
        self.fields['new_password1'].label = ''
        self.fields['new_password2'].label = ''

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'

        self.fields['old_password'].widget.attrs['style'] = 'font-size: 20px'
        self.fields['new_password1'].widget.attrs['style'] = 'font-size: 20px'
        self.fields['new_password2'].widget.attrs['style'] = 'font-size: 20px'

        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'

        self.fields['new_password1'].help_text = ''

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')