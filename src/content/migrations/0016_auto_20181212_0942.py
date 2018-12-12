# Generated by Django 2.1.3 on 2018-12-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_auto_20181211_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcontent',
            name='purpose',
            field=models.CharField(choices=[('email_verification', 'Email verification'), ('forgot_password', 'Forgot password'), ('successful_email_verification', 'Successful email verification'), ('successful_phone_verification', 'Successful phone verification'), ('successful_id_verification', 'Successful ID verification'), ('failed_id_verification', 'Failed ID verification'), ('successful_selfie_verification', 'Successful selfie verification'), ('failed_selfie_verification', 'Failed selfie verification'), ('gift_promotion', 'Gift promotion'), ('coin_price', 'Coin price'), ('successful_buying', 'Successful buying'), ('successful_selling', 'Successful selling'), ('api_reference', 'API Reference')], max_length=100),
        ),
    ]
