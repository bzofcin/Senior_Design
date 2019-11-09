from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import stock_data

def main(request):
    data = {'authenticated': True}
    return render(request,'stockpicker/main.html', data)

def portfolio(request):
    data = {'authenticated': True}
    return render(request,'stockpicker/portfolio.html', data)

def purchase(request):
    #data = {'authenticated': True}

    if request.method == 'POST':
        a = stock_data()
        a.company = request.POST['company']
        a.save();
    #    a = Question()
        #a.question_text = request.POST['question_text']
        #a.pub_date = datetime.date.today()
        #a.save()

    return redirect('portfolio')


def dashboard(request):
    data = {'authenticated': True}
    return render(request,'layouts/dashboard_layout.html', data)
