# Generated by Django 3.2.3 on 2021-05-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20210530_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]