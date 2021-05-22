from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Account(models.Model):
    account_number = models.CharField(max_length=40)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number
