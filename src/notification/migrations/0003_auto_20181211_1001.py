# Generated by Django 2.1.3 on 2018-12-11 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20181205_0300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemnotification',
            options={'verbose_name': 'Notification', 'verbose_name_plural': 'Notifications'},
        ),
        migrations.AlterModelOptions(
            name='systemreminder',
            options={'verbose_name': 'Reminder', 'verbose_name_plural': 'Reminders'},
        ),
        migrations.AlterModelOptions(
            name='systemreminderaction',
            options={'verbose_name': 'Reminder Action', 'verbose_name_plural': 'Reminder Actions'},
        ),
    ]