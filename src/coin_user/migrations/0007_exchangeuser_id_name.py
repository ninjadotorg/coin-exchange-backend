# Generated by Django 2.1.3 on 2018-11-19 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_user', '0006_auto_20181119_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangeuser',
            name='id_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]