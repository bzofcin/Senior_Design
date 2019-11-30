from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.sessions.models import Session
import json
import feedparser
locu_api = 'YOUR KEY HERE'
import csv
from .models import portfolio
import datetime
#import feedparser
import requests
import os


from collections import defaultdict

########################################################################################################
# Trends
########################################################################################################

def trends(request):
    if request.method == 'POST':   # when you post a form
        data = ''

    return render(request,'stockpicker/stock_trends.html', {})


def get_context_data(self, item, **kwargs):
    context = super().get_context_data(**kwargs)
    context['author'] = item.author
    print(context['author'])
    return context


########################################################################################################
# Main Page - Ivy B.
########################################################################################################

@login_required
def main(request):
    data = {'authenticated': True}
    return render(request,'stockpicker/main.html', data)

########################################################################################################
# Research  - Ivy B.
########################################################################################################

@login_required
def research(request):

    if request.method == 'POST':
        path = '/home/unlvteamseven/aistockpicker/static/predictions/Facebook.csv'
        timeStamp = []
        closePrice = []
        openPrice = []
        volume = []
        with open(path) as csvfile:
            inputcsv = csv.reader(csvfile, delimiter=',')
            for row in inputcsv:
                timeStamp.append(row[0:1])
                openPrice.append(row[1:2])
                closePrice.append(row[2:3])
                volume.append(row[3:4])

        api_key = locu_api
        company = request.POST['company'].upper()
        url = 'https://www.nasdaq.com/feed/rssoutbound?symbol=' + company
        data = feedparser.parse(url)
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/' + company)
        stockdata = response.json()
        historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/' + company + '?serietype=line')
        historical_stockdata = historical_response.json()

        return render(request,'stockpicker/stock_purchase.html', {'data': data,
                                                                  'symbol': stockdata['symbol'],
                                                                  'price': stockdata['price'],
                                                                  'timeStamp': timeStamp,
                                                                  'closePrice': closePrice,
                                                                  'openPrice': openPrice,
                                                                  'volume': volume,
                                                                  'historical_stockdata': historical_stockdata,
                                                                  'authenticated': True})
    else:
        api_key = locu_api
        url = 'https://www.nasdaq.com/feed/rssoutbound'
        data = feedparser.parse(url)
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL')
        stockdata = response.json()
        historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line')
        historical_stockdata = historical_response.json()

    return render(request,'stockpicker/stock_purchase.html', {'data': data,
                                                              'symbol': stockdata['symbol'],
                                                              'price': stockdata['price'],
                                                              'historical_stockdata': historical_stockdata,
                                                              'authenticated': True})


########################################################################################################
# Show My Portfolio and Stocks  - Ivy B.
########################################################################################################

@login_required
def myportfolio(request):
    if request.method == 'POST':
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/' + company)
        stockdata = response.json()
        historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/' + company + '?serietype=line')
        historical_stockdata = historical_response.json()

    current_user = request.user
    data = portfolio.objects.filter(user_id=current_user.id)

    context = {'authenticated': True, 'userPorfolio': data}
    return render(request,'stockpicker/showportfolio.html', context)

########################################################################################################
# Purchase -> Redirects back to Portfolio  - Ivy B.
########################################################################################################

@login_required
def purchase(request):
    current_user = request.user
    if request.method == 'POST':
        a = portfolio()
        a.user_id = current_user.id
        a.user_name = current_user.username
        a.company = request.POST['company'].upper()
        a.price = 31.33
        a.shares = request.POST['shares']
        a.purchase_timestamp = datetime.date.today()
        a.save()

    return redirect('myportfolio')

########################################################################################################
# Stock Info - Ivy B.
########################################################################################################

@login_required
def stockinfo(request):
    responseList = requests.get('https://financialmodelingprep.com/api/v3/company/stock/list')
    stocklist = responseList.json()

    if request.method == 'POST':
        api_key = locu_api
        company = request.POST['company'].upper()
        url = 'https://www.nasdaq.com/feed/rssoutbound?symbol=' + company
        data = feedparser.parse(url)
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/' + company)
        stockdata = response.json()
        historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/' + company + '?timeseries=1')
        historical_stockdata = historical_response.json()
        showBuyForm = True
        return render(request,'stockpicker/stock_information.html', {'data': data,
                                                                  'symbol': stockdata['symbol'],
                                                                  'price': stockdata['price'],
                                                                  'showBuyForm': showBuyForm,
                                                                  'historical_stockdata': historical_stockdata,
                                                                  'stocklist': stocklist,
                                                                  'authenticated': True})
    else:
        showBuyForm = False
        api_key = locu_api
        url = 'https://www.nasdaq.com/feed/rssoutbound'
        data = feedparser.parse(url)
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL')
        stockdata = response.json()
        historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?timeseries=1')
        historical_stockdata = historical_response.json()

        return render(request,'stockpicker/stock_information.html', {'data': data,
                                                              'symbol': stockdata['symbol'],
                                                              'price': stockdata['price'],
                                                              'showBuyForm': showBuyForm,
                                                              'stocklist': stocklist,
                                                              'historical_stockdata': historical_stockdata,
                                                              'authenticated': True})

########################################################################################################
# Sell -> Redirects back to Portfolio  - Ivy B.
########################################################################################################

@login_required
def sell(request, id):
    mportfolio = portfolio.objects.get(id=id)
    mportfolio.delete()
    return redirect('myportfolio')

########################################################################################################
# Dashboard - Not Used  - Ivy B.
########################################################################################################

@login_required
def dashboard(request):
    data = {'authenticated': True}
    return render(request,'layouts/dashboard_layout.html', data)
