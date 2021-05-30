from django.db import models
from djmoney.models.fields import MoneyField


class TransactionTypes(models.TextChoices):
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"


class Bank(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    account_number = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=100, default="")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    balance = MoneyField(
        max_digits=14, decimal_places=2, default_currency="KRW", null=True, blank=True
    )
    balance_updated = models.DateTimeField(null=True, blank=True)
    open_date = models.DateField()
    close_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    transaction_added = models.BooleanField(default=False)
    is_mine = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_number


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True)
    note = models.CharField(max_length=20, default="", blank=True)
    balance = MoneyField(
        max_digits=14, decimal_places=2, default_currency="KRW", null=True, blank=True
    )
    transaction_from_amount = MoneyField(
        max_digits=14, decimal_places=2, default_currency="KRW", null=True, blank=True
    )
    transaction_to_amount = MoneyField(
        max_digits=14, decimal_places=2, default_currency="KRW", null=True, blank=True
    )
    transaction_type = models.CharField(max_length=10, choices=TransactionTypes.choices)
