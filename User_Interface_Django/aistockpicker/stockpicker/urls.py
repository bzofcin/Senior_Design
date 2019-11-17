from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('main', views.main, name='main'),
    path('myportfolio', views.myportfolio, name='myportfolio'),
    #path('sell/<int:id>/', views.sell, name='sell'),
    url(r'^sell/(?P<id>\d+)/', views.sell, name='sell'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('purchase', views.purchase, name='purchase'),
    path('research', views.research, name='research'),

]

