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
from .models import portfolio, account, predictions, companylist
import datetime
#import feedparser
import requests
import os
import pandas as pd
from django import template
register = template.Library()
from collections import defaultdict
from django.utils.dateparse import parse_date
from django.utils.formats import get_format

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

########################################################################################################
# Trends
########################################################################################################

def trends(request):
    if request.method == 'POST':   # when you post a form
        data = pd.read_csv('/home/unlvteamseven/aistockpicker/static/predictions/Amazon.com Inc.csv')
        print(data.head(5))

    return render(request,'stockpicker/stock_trends.html', {})


def get_context_data(self, item, **kwargs):
    context = super().get_context_data(**kwargs)
    context['author'] = item.author
    print(context['author'])
    return context



@register.simple_tag
def define(val=None):
  return val

@register.simple_tag
def mult(a, b):
    return a * b

########################################################################################################
# Main Page - Ivy B.
########################################################################################################

@login_required
def main(request):

    current_user = request.user
    porfolioData = portfolio.objects.filter(user_id=current_user.id)
    userAccount = account.objects.only('credits').get(user_id=current_user.id).credits
    credits = userAccount


    # Purchased before then just get the credit balance
    if account.objects.filter(user_id=current_user.id).exists():
        userAccount = account.objects.only('credits').get(user_id=current_user.id).credits
        credits = userAccount
    else: # If this is a new account that has never purchased stock - Start with 100k credit
        a = account()
        a.user_id = current_user.id
        a.user_name = current_user.username
        a.credits = 100000.00
        a.save()


    arrayData = []
    portfolioValue = 0
    valueTotal = 0


    for item in porfolioData:
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/' + item.company)
        stockdata = response.json()
        arrayData.append(stockdata['price'])
        portfolioValue = portfolioValue + (stockdata['price'] * item.shares)

    valueTotal = credits + portfolioValue


    url = 'https://www.nasdaq.com/feed/rssoutbound?category=Artificial+Intelligence'
    feeddata = feedparser.parse(url)
    response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL')
    stockdata = response.json()


    return render(request,'stockpicker/main.html', {'data': feeddata,
                                                          'symbol': stockdata['symbol'],
                                                          'price': stockdata['price'],
                                                          'credits': credits,
                                                          'userPorfolio': porfolioData,
                                                          'arrayData': arrayData,
                                                          'valueTotal': valueTotal,
                                                          'portfolioValue': portfolioValue,
                                                          'authenticated': True})


########################################################################################################
# Research  - Ivy B.
########################################################################################################

@login_required
def research(request):

    if request.method == 'POST':
        company = request.POST['company']
        res = predictions.objects.filter(stockname=company).order_by('timestamp')
        return render(request,'stockpicker/stock_purchase.html', {'res': res,
                                                                  'company':company,
                                                                  'authenticated': True})
    else:
        company = 'Apple Inc'
        res = predictions.objects.filter(stockname='Apple Inc').order_by('timestamp')

    return render(request,'stockpicker/stock_purchase.html', {'res': res,
                                                              'company': company,
                                                              'authenticated': True})


########################################################################################################
# Show My Portfolio and Stocks  - Ivy B.
########################################################################################################

@login_required
def myportfolio(request):
    responseList = requests.get('https://financialmodelingprep.com/api/v3/company/stock/list')
    stocklist = responseList.json()
    current_user = request.user

    # Purchased before then just get the credit balance
    if account.objects.filter(user_id=current_user.id).exists():
        userAccount = account.objects.only('credits').get(user_id=current_user.id).credits
        credits = userAccount
    else: # If this is a new account that has never purchased stock - Start with 100k credit
        a = account()
        a.user_id = current_user.id
        a.user_name = current_user.username
        a.credits = 100000.00
        a.save()
    if request.method == 'POST':
        company = request.POST['company'].upper()
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/' + company)
        stockdata = response.json()
        historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/' + company + '?serietype=line')
        historical_stockdata = historical_response.json()


    current_user = request.user
    porfolioData = portfolio.objects.filter(user_id=current_user.id)

    userAccount = account.objects.only('credits').get(user_id=current_user.id).credits
    credits = userAccount

    arrayData = []
    portfolioValue = 0
    valueTotal = 0
    for item in porfolioData:
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/' + item.company)
        stockdata = response.json()
        arrayData.append(stockdata['price'])
        portfolioValue = portfolioValue + (stockdata['price'] * item.shares)

    valueTotal = credits + portfolioValue


    if request.method == 'POST':
        company = request.POST['company'].upper()
        url = 'https://www.nasdaq.com/feed/rssoutbound?symbol=' + company
        feeddata = feedparser.parse(url)
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/' + company)
        stockdata = response.json()
        historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/' + company + '?timeseries=1')
        historical_stockdata = historical_response.json()
        showBuyForm = True
        return render(request,'stockpicker/showportfolio.html', {'data': feeddata,
                                                                  'symbol': stockdata['symbol'],
                                                                  'price': stockdata['price'],
                                                                  'userPorfolio': porfolioData,
                                                                  'arrayData': arrayData,
                                                                  'valueTotal': valueTotal,
                                                                  'portfolioValue': portfolioValue,
                                                                  'credits': credits,
                                                                  'company': company,
                                                                  'showBuyForm': showBuyForm,
                                                                  'historical_stockdata': historical_stockdata,
                                                                  'stocklist': stocklist,
                                                                  'authenticated': True})
    else:
        showBuyForm = False
        url = 'https://www.nasdaq.com/feed/rssoutbound'
        feeddata = feedparser.parse(url)
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL')
        stockdata = response.json()
        historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?timeseries=1')
        historical_stockdata = historical_response.json()

        return render(request,'stockpicker/showportfolio.html', {'data': feeddata,
                                                              'symbol': stockdata['symbol'],
                                                              'price': stockdata['price'],
                                                              'credits': credits,
                                                              'userPorfolio': porfolioData,
                                                              'arrayData': arrayData,
                                                              'valueTotal': valueTotal,
                                                              'portfolioValue': portfolioValue,
                                                              'showBuyForm': showBuyForm,
                                                              'stocklist': stocklist,
                                                              'historical_stockdata': historical_stockdata,
                                                              'authenticated': True})





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
        a.purchase_price = request.POST['price'].upper()
        a.shares = request.POST['shares']
        a.purchase_timestamp = datetime.date.today()
        a.save()

        userAccount = account.objects.only('credits').get(user_id=current_user.id).credits
        credits = userAccount
        price = float(request.POST['price'])
        shares = float(request.POST['shares'])
        purchaseAmount =  price * shares

        obj = account.objects.get(user_id = current_user.id)
        obj.credits = credits - purchaseAmount
        obj.save()

    return redirect('myportfolio')

########################################################################################################
# Stock Info - Ivy B.
########################################################################################################

@login_required
def stockinfo(request):
    responseList = requests.get('https://financialmodelingprep.com/api/v3/company/stock/list')
    stocklist = responseList.json()
    current_user = request.user

    # Purchased before then just get the credit balance
    if account.objects.filter(user_id=current_user.id).exists():
        userAccount = account.objects.only('credits').get(user_id=current_user.id).credits
        credits = userAccount
    else: # If this is a new account that has never purchased stock - Start with 100k credit
        a = account()
        a.user_id = current_user.id
        a.user_name = current_user.username
        a.credits = 100000.00
        a.save()
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
                                                                  'credits': credits,
                                                                  'company': company,
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
                                                              'credits': credits,
                                                              'showBuyForm': showBuyForm,
                                                              'stocklist': stocklist,
                                                              'historical_stockdata': historical_stockdata,
                                                              'authenticated': True})

########################################################################################################
# CANCEL -> Redirects back to Portfolio  - Ivy B.
########################################################################################################

@login_required
def cancel(request):
    return redirect('myportfolio')

########################################################################################################
# Sell -> Redirects back to Portfolio  - Ivy B.
########################################################################################################

@login_required
def sell(request, id):
    current_user = request.user
    mportfolio = portfolio.objects.get(id=id)
    userAccount = account.objects.only('credits').get(user_id=current_user.id).credits
    credits = userAccount
    price = float(mportfolio.purchase_price)
    shares = float(mportfolio.shares)
    soldAmount =  price * shares
    obj = account.objects.get(user_id = current_user.id)
    obj.credits = credits + soldAmount
    obj.save()
    mportfolio.delete()

    return redirect('myportfolio')

########################################################################################################
# Dashboard - Not Used  - Ivy B.
########################################################################################################

@login_required
def dashboard(request):
    data = {'authenticated': True}
    return render(request,'layouts/dashboard_layout.html', data)




'''
    response = requests.get('https://financialmodelingprep.com/api/v3/company/stock/list')
    companydata = response.json()
    for symbols in companydata:
        for item in symbols.symbolsList:
            c = companylist()
            c.symbol = item.symbol
            c.company = item.name
            c.save()
'''
