from django.db import models
from datetime import datetime
from django.utils import timezone

class stock_data(models.Model):
    id = models.BigIntegerField(primary_key=True)
    company =  models.CharField(max_length=100)
    ticker_symbol =  models.CharField(max_length=4)
    timestamp =  models.CharField(max_length=30)
    open = models.FloatField(default=0.0)
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    close = models.FloatField(default=0.0)
    volume = models.IntegerField(default=0)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
