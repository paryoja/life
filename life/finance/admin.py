from django.contrib import admin

from . import models


# Inlines
class BankInline(admin.TabularInline):
    model = models.Bank


class AccountInline(admin.TabularInline):
    model = models.Account


class TransactionInline(admin.TabularInline):
    model = models.Transaction


# Admins
@admin.register(models.Bank)
class BankAdmin(admin.ModelAdmin):
    inline = [AccountInline]


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "account_number",
        "description",
        "open_date",
        "close_date",
        "is_active",
        "transaction_added",
        "is_mine",
    )


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "balance",
        "transaction_type",
        "transaction_from_amount",
        "transaction_from_amount_currency",
    )
