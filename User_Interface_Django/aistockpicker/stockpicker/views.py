from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.sessions.models import Session

import feedparser
locu_api = 'YOUR KEY HERE'

from .models import portfolio
import datetime
#import feedparser

def get_context_data(self, item, **kwargs):
    context = super().get_context_data(**kwargs)
    context['author'] = item.author
    print(context['author'])
    return context

@login_required
def main(request):
    data = {'authenticated': True}
    return render(request,'stockpicker/main.html', data)

@login_required
def research(request):
    if request.method == 'POST':
        api_key = locu_api
        company = request.POST['company'].upper()
        url1= 'http://johnsmallman.wordpress.com/author/johnsmallman/feed/'
        url = 'https://www.nasdaq.com/feed/rssoutbound?symbol=' + company
        json_obj = feedparser.parse(url)
        info = json_obj['feed'][0]['title_detail']
        link = json_obj.headers.get('content-type')
        #data = json.load(json_obj)
        #for item in data['objects']:
            #print(item['name'], item['phone']
        return render(request,'stockpicker/stock_purchase.html', {'data': json_obj, inf: info, lin: link,   'authenticated': True})
    else:
        api_key = locu_api
        url = 'https://www.nasdaq.com/feed/rssoutbound?symbol=AMZN'
        data = feedparser.parse(url)

    return render(request,'stockpicker/stock_purchase.html', {'data': data, 'authenticated': True})


def myportfolio(request):
    link = 'http://finance.yahoo.com/rss/headline?s=yhoo'
  #  foo = feedparser.parse(link)
  #  feed = foo['feed']
  #  title = feed['title']

    context = {'authenticated': True, 'userPorfolio': portfolio.objects.all()}
    return render(request,'stockpicker/showportfolio.html', context)

@login_required
def purchase(request):

    if request.method == 'POST':
        a = portfolio()
        a.user_id = 1
        a.user_name = 'Test User'
        a.company = request.POST['company'].upper()
        a.price = 31.33
        a.shares = request.POST['shares']
        a.purchase_timestamp = datetime.date.today()
        a.save()

    return redirect('myportfolio')

@login_required
def sell(request, id):
    mportfolio = portfolio.objects.get(id=id)
    mportfolio.delete()
    return redirect('myportfolio')

@login_required
def dashboard(request):
    data = {'authenticated': True}
    return render(request,'layouts/dashboard_layout.html', data)
