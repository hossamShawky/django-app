from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Post

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['desc']

