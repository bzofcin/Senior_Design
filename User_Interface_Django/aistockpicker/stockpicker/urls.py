from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('main', views.main, name='main'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('purchase', views.purchase, name='purchase'),
]

