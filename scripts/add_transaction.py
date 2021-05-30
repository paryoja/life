import pandas as pd

from life.finance.models import Account, Money, Transaction

excel_names = [
    "거래내역조회-자유_20210530_052348.xls",
    "거래내역조회-거치식_20210530_052327.xls",
    "거래내역조회-거치식_20210530_052316.xls",
    "거래내역조회-요구불_20210530_052113.xls",
    "거래내역조회-요구불_20210530_052258.xls",
]

keys = {
    "자유": {"created_at_date": "거래일자", "deposit_amount": "부금불입액"},
    "거치식": {"created_at_date": "거래일자", "deposit_amount": "이자지급액"},
    "요구불": {
        "created_at_date": "거래일자",
        "created_at_time": "거래시간",
        "note": "내용",
        "draw_amount": "찾으신금액",
        "deposit_amount": "맡기신금액",
    },
}
account_number_pos = {
    "자유": 5,
    "거치식": 7,
    "요구불": 5,
}

for name in excel_names:
    df = pd.read_excel(f"data/mg/{name}", skiprows=8)

    key_data = None
    account_pos = None
    for k in keys:
        if k in name:
            key_data = keys[k]
            account_pos = account_number_pos[k]
            break

    data = []
    for row in df.to_dict(orient="records"):

        data_object = {}
        for k, v in key_data.items():
            data_object[k] = row[v]

        data.append(data_object)

    df = pd.read_excel(f"data/mg/{name}")
    account_number = df.iloc[2][account_pos]

    acc = Account.objects.filter(account_number=account_number)[0]

    print(account_number)
    for d in data:
        if pd.isna(d["created_at_date"]):
            continue
        print(d)

        created_at = d["created_at_date"]
        if "created_at_time" in d:
            created_at += f" {d['created_at_time']}+09:00"
        else:
            created_at += " 00:00+09:00"
        created_at = created_at.replace(".", "-")
        print(created_at)

        transaction_type = None
        if not pd.isna(d["deposit_amount"]):
            transaction_type = "Deposit"
            amount = d["deposit_amount"]
        elif not pd.isna(d["draw_amount"]):
            transaction_type = "Withdraw"
            amount = d["draw_amount"]
        else:
            continue

        note = ""
        if "note" in d and not pd.isna(d["note"]):
            note = d["note"]

        money_filter = Money.objects.filter(amount=amount, currency="KRW")
        money_obj = None
        if money_filter.exists():
            money_obj = money_filter[0]
        else:
            money_obj = Money(amount=amount, currency="KRW").save()
        transaction = Transaction(
            account=acc,
            note=note,
            created_at=created_at,
            transaction_from_amount=money_obj,
            transaction_type=transaction_type,
        )
        transaction.save()
