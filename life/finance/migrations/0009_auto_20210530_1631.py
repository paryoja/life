# Generated by Django 3.2.3 on 2021-05-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_alter_account_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='close_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='open_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]