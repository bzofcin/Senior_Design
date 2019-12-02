from django.db import models
from datetime import datetime
from django.utils import timezone

class portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    user_id =  models.IntegerField(default=0)
    user_name =  models.CharField(max_length=100)
    company =  models.CharField(max_length=100)
    shares =  models.IntegerField(default=0)
    ticker_symbol =  models.CharField(max_length=4)
    purchase_timestamp =  models.DateField(max_length=30)
    purchase_price = models.FloatField(default=0.0)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)

class stock_data(models.Model):
    id = models.AutoField(primary_key=True)
    company =  models.CharField(max_length=100)
    ticker_symbol =  models.CharField(max_length=4)
    timestamp =  models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    volume = models.IntegerField(default=0)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
