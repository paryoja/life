# Generated by Django 3.2.3 on 2021-05-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_alter_account_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.ManyToManyField(blank=True, to='finance.Money'),
        ),
    ]
