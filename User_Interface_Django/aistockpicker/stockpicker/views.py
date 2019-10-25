from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import JsonResponse


def main(request):
    data = {'authenticated': True}
    return render(request,'stockpicker/main.html', data)


def dashboard(request):
    data = {'authenticated': True}
    return render(request,'layouts/dashboard_layout.html', data)
