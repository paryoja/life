# Generated by Django 3.2.3 on 2021-05-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0012_account_transaction_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_mine',
            field=models.BooleanField(default=True),
        ),
    ]