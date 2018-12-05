# Generated by Django 2.1.3 on 2018-12-05 03:18

import common.model_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coin_exchange', '0009_order_order_user_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='referralorder',
            name='tx_hash',
            field=common.model_fields.CryptoHashField(max_length=255, null=True),
        ),
    ]