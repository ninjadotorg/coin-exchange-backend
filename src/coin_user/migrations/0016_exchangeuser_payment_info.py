# Generated by Django 2.1.3 on 2018-12-03 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_user', '0015_exchangeuser_first_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangeuser',
            name='payment_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
