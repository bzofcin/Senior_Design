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
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import RegisterForm
from django.contrib.auth.models import User

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
           login(request)
           return redirect('stockpicker:myportfolio')

    return render(request,'accounts/login.html',{})


def loggedIn(request):

    return render(request,'accounts/loggedInScreen.html', {})

def registeration(request):

    if request.method == 'POST':
        form = UserCreationForm(request.username, request.POST)
        if form.is_valid():
            user = form.save()
            #update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'New Account Added!')
            return redirect('login')

        else:
            messages.error(request, 'Please correct the error below.')



    return render(request,'accounts/registration.html', {'authenticated': False, 'pass': 'Empty' })


def register(request):

     # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['password']
                )
                user.save()

                # Login the user
                login(request)

                # redirect to accounts page:
                return redirect('/stockpicker/myportfolio')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()


    return render(request,'accounts/registration.html', {'authenticated': False, 'form': form })

def about(request):

    return render(request,'accounts/about.html', {'authenticated': False })


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')









