# Generated by Django 2.2.5 on 2019-12-01 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockpicker', '0008_auto_20191201_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='close',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='high',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='low',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='open',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='volume',
            field=models.CharField(max_length=10),
        ),
    ]
