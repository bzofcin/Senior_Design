# Generated by Django 2.1 on 2019-11-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='myusers',
        ),
    ]