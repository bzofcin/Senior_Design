from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
    path('welcome', views.loggedIn, name='loggedIn')
]
