# Generated by Django 4.2.10 on 2024-02-25 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_request_alter_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date_and_time',
        ),
    ]