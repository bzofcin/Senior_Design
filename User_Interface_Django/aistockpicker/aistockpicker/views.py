from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import JsonResponse
from urllib import request
import urllib
from datetime import datetime, timedelta
from datetime import datetime
import requests
import json
import feedparser

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)


def plotly_scatter(df, _x):
    x = df.iloc[:, 1:2]
    y = df.iloc[:, 3:4]

    trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10},
                        mode="lines",  name='1st Trace')

    data=go.Data([trace1])
    layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
    figure=go.Figure(data=data,layout=layout)
    div = py.plot(figure, auto_open=False, output_type='div')

    return div

def home(request):

    url = 'https://www.nasdaq.com/feed/rssoutbound?category=Artificial+Intelligence'
    rssdata = feedparser.parse(url)

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


    historical_response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/GOOG?from=2019-10-28&to=2019-11-28')
    historical_stockdata = historical_response.json()



    #return JsonResponse({'mystring':"return this string"})

    return render(request,'accounts/home.html', {'authenticated': False,
                                                 'historical_stockdata': historical_stockdata,
                                                 'current_date': current_date,
                                                 'rssdata': rssdata,
                                                 'start_date': start_date,
                                                 'last_month_text': last_month_text,
                                                 'last_year_full': last_year_full,
                                                 'last_day_full': last_day_full,
                                                 'current_month_text': current_month_text,
                                                 'current_year_full': current_year_full,
                                                 'current_day_full': current_day_full})
