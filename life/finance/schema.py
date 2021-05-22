import graphene
from graphene_django import DjangoObjectType, fields

from .models import Bank, Account


class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        fields = ("id", "name", "accounts")


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        fields = ("id", "account_number", "bank")


class Query(graphene.ObjectType):
    all_accounts = graphene.List(AccountType)
    bank_by_name = graphene.Field(BankType, name=graphene.String(required=True))

    def resolve_all_accounts(root, info):
        return Account.objects.select_related("bank").all()

    def resolve_bank_by_name(root, info, name):
        try:
            return Bank.objects.get(name=name)
        except Bank.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
