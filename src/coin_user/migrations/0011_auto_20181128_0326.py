# Generated by Django 2.1.3 on 2018-11-28 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_user', '0010_auto_20181127_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangeuser',
            name='language',
            field=models.CharField(choices=[('km', '🇰🇭 ភាសាខ្មែរ'), ('en', '🇺🇸 English'), ('id', '🇮🇩 bahasa Indonesia'), ('hk', '🇭🇰 廣東話')], max_length=10, null=True),
        ),
    ]
