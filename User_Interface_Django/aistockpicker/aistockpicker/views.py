from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import JsonResponse
from urllib import request
import urllib
import json
import requests
from datetime import datetime, timedelta

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def home(request):
    today = datetime.today()
    date_N_days_ago = datetime.now() - timedelta(days=30)

    last_month_text = date_N_days_ago.strftime('%B')
    last_year_full = date_N_days_ago.strftime('%Y')
    last_day_full = date_N_days_ago.strftime('%d')

    current_month_text = datetime.now().strftime('%B')
    current_year_full = datetime.now().strftime('%Y')
    current_day_full = datetime.now().strftime('%d')


    last_month = date_N_days_ago.strftime('%m')
    last_year = date_N_days_ago.strftime('%Y')
    last_day = date_N_days_ago.strftime('%d')

    current_date = datetime.now().strftime('%Y-%m-%d')
    start_date = date_N_days_ago.strftime('%Y-%m-%d')

    #2019-10-28
#    startDate = last_year +
    historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/GOOG?from=2019-10-28&to=2019-11-28')
    historical_stockdata = historical_response.json()

    #return JsonResponse({'mystring':"return this string"})
    return render(request,'accounts/home.html', {'authenticated': False,
                                                 'historical_stockdata': historical_stockdata,
                                                 'current_date': current_date,
                                                 'start_date': start_date,
                                                 'last_month_text': last_month_text,
                                                 'last_year_full': last_year_full,
                                                 'last_day_full': last_day_full,
                                                 'current_month_text': current_month_text,
                                                 'current_year_full': current_year_full,
                                                 'current_day_full': current_day_full})
