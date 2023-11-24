from django.urls import path
from app import views

from .views import * # all views in app
urlpatterns = [
    path('', views.index, name='index'),
    path('all/  ', views.all, name='all'),

]
