from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')

        labels = {
            'title': '',
            'author': '',
            'body': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: 20px;', 'placeholder': 'Title...'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: 20px;', 'value': '', 'type': 'hidden', 'id': 'author'}),
            'body': forms.Textarea(attrs={'class': 'form-control body', 'placeholder': 'Type your content here....', 'style': 'display:none'})
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        labels = {
            'title': '',
            'body': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: 20px;', 'placeholder': 'Title...'}),
            'body': forms.Textarea(attrs={'class': 'form-control body', 'placeholder': 'Type your content here....', 'style': 'display:none'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
    
        labels = {
            'name': '',
            'body': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control author d-none', 'style': 'font-size: 20px;', 'placeholder': 'Name...'}),
            'body': forms.Textarea(attrs={'class': 'form-control body d-none', 'placeholder': 'Type your content here....', 'style': 'display:none'})
        }