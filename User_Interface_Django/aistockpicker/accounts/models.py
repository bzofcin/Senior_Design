from django.db import models

# Create your models here.

class users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    firstname =  models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    email =  models.CharField(max_length=100)
    password =  models.CharField(max_length=256)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)


class portfolio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    stock_symbol =  models.CharField(max_length=80)
    company = models.CharField(max_length=80)
    shares = models.IntegerField(default=0)
    buy_price =   models.FloatField(default=0.0)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
