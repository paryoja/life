from graphene import ObjectType, Schema, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Account, Bank, Transaction


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

    def resolve_balance(parent, info):
        return parent.balance.amount


class TransactionNode(DjangoObjectType):
    class Meta:
        model = Transaction
        filter_fields = {"account": ["exact"]}
        interfaces = (relay.Node,)

    def resolve_balance(parent, info):
        return parent.balance.amount

    def resolve_transaction_from_amount(parent, info):
        return parent.transaction_from_amount.amount

    def resolve_transaction_to_amount(parent, info):
        return parent.transaction_to_amount.amount


class Query(ObjectType):
    all_accounts = DjangoFilterConnectionField(AccountNode)
    account = relay.Node.Field(AccountNode)

    all_banks = DjangoFilterConnectionField(BankNode)
    bank = relay.Node.Field(BankNode)

    all_transactions = DjangoFilterConnectionField(TransactionNode)
    transaction = relay.Node.Field(TransactionNode)


schema = Schema(query=Query)
