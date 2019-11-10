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
from .models import myusers

import hmac, base64, struct, hashlib, time
import crypt, getpass, pwd
import urllib
import json
import datetime

from .models import users

def login(request):


    if request.method == 'POST':
        user = myusers()
        username = request.POST['username'].strip()
        password = request.POST['password']
        #password_hash = crypt.crypt(raw_password, 's0mRIdlKvIghsds131dsa9jlasdfj')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)

    return render(request,'accounts/login.html',{})


def loggedIn(request):

    return render(request,'accounts/loggedInScreen.html', {})

def register(request):

    if request.method == 'POST':
        user = myusers()
        user.username = request.POST['username'].strip()
        raw_password = request.POST['password']
        password_hash = crypt.crypt(raw_password, 's0mRIdlKvIghsds131dsa9jlasdfj')
        user.password = password_hash
        user.save()
        #login(request, user)
        return redirect('login')


    return render(request,'accounts/registration.html', {'authenticated': False, 'pass': 'Empty' })


def about(request):

    return render(request,'accounts/about.html', {'authenticated': False })

