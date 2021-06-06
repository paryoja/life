import json
import pathlib

import pandas

from life.finance.models import Account, Bank, Transaction, TransactionTypes

base = pathlib.Path("./data/sh")

sh = Bank.objects.filter(name="신한금융투자")[0]


def merge_data(prev, current):
    obj = {}
    for k, v in prev.items():
        obj[k[0]] = v
    for k, v in current.items():
        obj[k[1]] = v
    return obj


for path in base.glob("**/*.xls"):
    df = pandas.read_html(path)
    number = df[0][1][0].split()[0]

    acc = Account.objects.filter(account_number=number)
    if not acc:
        acc = Account(account_number=number, bank=sh)
        acc.save()
    else:
        acc = acc[0]

    df = pandas.read_html(path)

    count = 0
    datalist = df[1].to_dict("records")
    for data in datalist:
        if count % 2 == 0:
            prev_data = data
        else:
            merged = merge_data(prev_data, data)
            # print(merged)
            if merged["적요"] == "입금" or merged["적요"] == "은행이체입금":
                transaction_type = TransactionTypes.DEPOSIT
            elif merged["적요"] == "출금":
                transaction_type = TransactionTypes.WITHDRAW
            elif merged["적요"] == "매수" or merged["적요"] == "매수(수익증권)":
                transaction_type = TransactionTypes.BUY
            elif merged["적요"] == "매도" or merged["적요"] == "매도(수익증권)":
                transaction_type = TransactionTypes.SELL
            elif pandas.isna(merged["적요"]):
                if merged["구분"] == "배당세" or merged["구분"] == "예탁금이용료":
                    transaction_type = TransactionTypes.WITHDRAW
                elif merged["구분"] == "ETF분배금" or merged["구분"] == "분배금입금":
                    transaction_type = TransactionTypes.DEPOSIT
                elif merged["구분"] == "신탁매수":
                    # IRP 계좌에서 나오는 패턴
                    continue
                else:
                    print(merged)
                    print(merged["적요"], merged["구분"])
                    print(merged["적요"])
            elif merged["적요"] == "재투자매수":
                transaction_type = TransactionTypes.BUY
            elif merged["적요"] == "재투자환매":
                transaction_type = TransactionTypes.SELL
            else:
                print(merged["적요"])
            note = merged["구분"]
            balance = merged["최종금액"]
            transaction_from_amount = merged["변동금액"]

            if transaction_type == TransactionTypes.DEPOSIT:
                time = 0
            elif transaction_type == TransactionTypes.WITHDRAW:
                time = 3
            elif transaction_type == TransactionTypes.SELL:
                time = 1
            elif transaction_type == TransactionTypes.BUY:
                time = 2

            created_at = f"{merged['일자'].replace('.', '-')} 00:0{time}+09:00"

            tran = Transaction(
                account=acc,
                created_at=created_at,
                note=note,
                balance=balance,
                balance_currency="KRW",
                transaction_from_amount=transaction_from_amount,
                transaction_from_amount_currency="KRW",
                transaction_type=transaction_type,
                information=json.dumps(merged),
            )
            tran.save()
        count += 1
