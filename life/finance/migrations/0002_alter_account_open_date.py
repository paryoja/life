# Generated by Django 3.2.3 on 2021-05-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='open_date',
            field=models.DateField(),
        ),
    ]