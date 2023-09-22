
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = 'weather'
urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]