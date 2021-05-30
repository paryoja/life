from django.contrib import admin

from . import models


# Inlines
class BankInline(admin.TabularInline):
    model = models.Bank


class AccountInline(admin.TabularInline):
    model = models.Account


class MoneyInline(admin.TabularInline):
    model = models.Money


class TransactionInline(admin.TabularInline):
    model = models.Transaction


# Admins
@admin.register(models.Bank)
class BankAdmin(admin.ModelAdmin):
    inline = [AccountInline, MoneyInline]


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "account_number",
        "open_date",
        "close_date",
        "is_active",
        "transaction_added",
        "is_mine",
    )


@admin.register(models.Money)
class MoneyAdmin(admin.ModelAdmin):
    inline = [AccountInline, TransactionInline]


admin.site.register(models.Transaction)
