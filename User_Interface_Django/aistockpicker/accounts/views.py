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

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import RegisterForm
from django.contrib.auth.models import User, auth

import hmac, base64, struct, hashlib, time
import crypt, getpass, pwd
import urllib
import json
import datetime
import re
from urllib import request
#from .rssfeed import rssapi
import feedparser
locu_api = 'YOUR KEY HERE'
#import feedparser



def readapi(request):

   #rsf = rssapi.getfeed('')
    #locality = query.replace(' ', '%20')
    #final_url = url + "&locality=" + locality + "&category=restaurant"
    #final_url = url + "&category=restaurant"
    api_key = locu_api
    #url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    url = 'https://www.nasdaq.com/feed/rssoutbound?symbol=AMZN'
    #url2 = 'https://jsonplaceholder.typicode.com/posts'
    json_obj = feedparser.parse(url)
    #data = json.load(json_obj)

    #for item in data['objects']:
        #print(item['name'], item['phone']
    return render(request,'stockpicker/rssdump.html', {'data': json_obj})


def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('stockpicker/myportfolio')
        else:
            return render(request,'accounts/login.html', {'message': 'Wrong Username and Password', 'status' : 1})

    form = AuthenticationForm()
    return render(request,'accounts/login.html',{'status' : 0, 'message': ''})


def loggedIn(request):

    return render(request,'accounts/loggedInScreen.html', {})

def registered(request):

    return render(request,'accounts/registered.html', {'authenticated': False})


def register(request):
    status = 0
    message = ''

     # if this is a POST request we need to process the form data
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=request.POST['username']).exists():
                status = 1
                message = 'Username already exists!'
            else:
                user = form.save()
                return render(request, 'accounts/registration.html', {
                    'status': 2, 'message': 'You have been registered!.'
                })
                #return redirect('/accounts/login')
                return render(request, 'accounts/registration.html', {
                    'status': 1, 'message': 'Username already exists.'
                })
        else:
            return render(request,'accounts/registration.html', {'authenticated': False, 'status': 1, 'message': 'Error: Not valid entries. Make sure your passwords match.'})
    return render(request,'accounts/registration.html', {'authenticated': False, 'status': status, 'message': message})



def about(request):

    return render(request,'accounts/about.html', {'authenticated': False })


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')









