from django.db import models

# Create your models here.


class CurrencyType(models.TextChoices):
    KRW = "KRW"
    USD = "USD"


class TransactionTypes(models.TextChoices):
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"


class Bank(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Money(models.Model):
    amount = models.FloatField()
    currency = models.CharField(max_length=3, choices=CurrencyType.choices)

    def __str__(self):
        return f"{self.amount} {self.currency}"


class Account(models.Model):
    account_number = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=100, default="")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    balance = models.ManyToManyField(Money, blank=True)
    open_date = models.DateField(null=True, blank=True)
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
    note = models.CharField(max_length=20, default="")
    transaction_from_amount = models.ForeignKey(
        Money,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transaction_from",
    )
    transaction_to_amount = models.ForeignKey(
        Money,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transaction_to",
    )
    transaction_type = models.CharField(max_length=10, choices=TransactionTypes.choices)
