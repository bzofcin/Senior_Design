from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import JsonResponse

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def home(request):
    data = {}
    #return JsonResponse({'mystring':"return this string"})
    return render(request,'accounts/home.html', data)
