from life.finance.models import Bank

data = [
    "코인원",
    "삼성화재",
    "삼성생명",
    "NH투자증권",
    "KB증권",
    "신한금융투자",
    "대신증권",
    "삼성증권",
    "새마을금고",
    "농협",
    "카카오뱅크",
]

for d in data:
    bank = Bank(name=d)
    bank.save()
