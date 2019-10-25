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



def login(request):

    return render(request,'accounts/login.html', {})

def loggedIn(request):

    return render(request,'accounts/loggedInScreen.html', {})

def register(request):

    return render(request,'accounts/registration.html', {'authenticated': False })


def about(request):

    return render(request,'accounts/about.html', {'authenticated': False })


def login_norecaptcha(request):
    if request.user.is_authenticated():
        return redirect('home')


    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        request.session['username'] = username
        user = authenticate(username=username, password=password)
        if user is not None:
        	if user.is_active:
        		auth_login(request, user)
        		return redirect('home')

        else:

        	return render(request, 'accounts/login.html', {'errormsg': "Invalid Username & Password"})


    return render(request, 'auth/sa_login.html', {})
