from django.db import models

# Create your models here.



class portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    stock_symbol =  models.CharField(max_length=80)
    company = models.CharField(max_length=80)
    shares = models.IntegerField(default=0)
    buy_price =   models.FloatField(default=0.0)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)

