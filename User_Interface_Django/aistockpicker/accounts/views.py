from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import JsonResponse


def login(request):
    data = {}
    return render(request,'accounts/login.html', data)


def register(request):
    data = {}
    return render(request,'accounts/registration.html', data)
