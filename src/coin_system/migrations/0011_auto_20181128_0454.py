# Generated by Django 2.1.3 on 2018-11-28 04:54

import common.model_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coin_system', '0010_auto_20181128_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrydefaultconfig',
            name='language',
            field=common.model_fields.LanguageField(choices=[('km', '🇰🇭 ភាសាខ្មែរ'), ('en', '🇺🇸 English'), ('id', '🇮🇩 bahasa Indonesia'), ('zh-Hant-HK', '🇭🇰 廣東話')], max_length=10),
        ),
    ]