# Generated by Django 3.2.3 on 2021-05-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_alter_account_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='transaction_added',
            field=models.BooleanField(default=False),
        ),
    ]