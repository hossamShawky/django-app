from django.shortcuts import render
from django.http import HttpResponse
from app.models import User
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def all(request):
    users = User.objects.all()
    return render(request, 'users.html', context={"users": users})    




