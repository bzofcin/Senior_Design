from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
#from .models import Users

import hmac, base64, struct, hashlib, time

import urllib
import json
import datetime


def login(request):


    if request.method == 'POST':
        email = request.POST['email']
        password= request.POST['password']
        confirmPassword= request.POST['confirmpassword']
 #       a = Users()
 #       a.email = email
 #       a.password=password
 #       a.save()

    return render(request,'accounts/login.html',{})


def loggedIn(request):

    return render(request,'accounts/loggedInScreen.html', {})

def register(request):

    #if request.method == 'POST':

        #username = form.cleaned_data.get('username')
        #raw_password = form.cleaned_data.get('password1')
        #user =
        #login(request, user)
        #return redirect('home')


    return render(request,'accounts/registration.html', {'authenticated': False })


def about(request):

    return render(request,'accounts/about.html', {'authenticated': False })

