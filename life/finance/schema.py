from graphene import ObjectType, Schema, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Account, Bank, Money, Transaction


class BankNode(DjangoObjectType):
    class Meta:
        model = Bank
        filter_fields = {"name": ["exact"]}
        interfaces = (relay.Node,)


class AccountNode(DjangoObjectType):
    class Meta:
        model = Account
        filter_fields = {
            "account_number": ["exact"],
            "bank": ["exact"],
            "is_mine": ["exact"],
        }
        interfaces = (relay.Node,)


class TransactionNode(DjangoObjectType):
    class Meta:
        model = Transaction
        filter_fields = {"account": ["exact"]}
        interfaces = (relay.Node,)


class MoneyNode(DjangoObjectType):
    class Meta:
        model = Money
        filter_fields = ["amount"]
        interfaces = (relay.Node,)


class Query(ObjectType):
    all_accounts = DjangoFilterConnectionField(AccountNode)
    account = relay.Node.Field(AccountNode)

    all_banks = DjangoFilterConnectionField(BankNode)
    bank = relay.Node.Field(BankNode)

    all_transactions = DjangoFilterConnectionField(TransactionNode)
    transaction = relay.Node.Field(TransactionNode)


schema = Schema(query=Query)
