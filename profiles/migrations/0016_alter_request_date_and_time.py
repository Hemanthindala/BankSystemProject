# Generated by Django 4.2.10 on 2024-02-25 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_transaction_date_and_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]