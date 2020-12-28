from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms as f
from .models import Article
from .models import Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['producer', 'model']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

