from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import JsonResponse


def main(request):
    data = {}
    return render(request,'stockpicker/main.html', data)
