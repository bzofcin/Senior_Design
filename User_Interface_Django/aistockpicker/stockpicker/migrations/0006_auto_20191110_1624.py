# Generated by Django 2.1 on 2019-11-10 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockpicker', '0005_auto_20191110_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_data',
            name='close',
        ),
        migrations.RemoveField(
            model_name='stock_data',
            name='high',
        ),
        migrations.RemoveField(
            model_name='stock_data',
            name='low',
        ),
    ]