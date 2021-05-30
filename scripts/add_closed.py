from life.finance.models import Account, Bank

lines_per_record = 5

mg = Bank.objects.filter(name="새마을금고")[0]


def format_date(date):
    return date.replace(".", "-")


def format_won(amount):
    return amount.replace("원", "").replace(",", "")


with open("./scripts/closed.txt") as f:
    index = 0

    title = ""
    account_number = ""
    open_date = ""
    close_date = ""
    original_amount = ""
    actual_amount = ""
    interest = ""

    for line in f:
        print(index, line)
        if index == 0:
            title = line.split()[1]
        if index == 1:
            account_number, open_date = line.split()
        if index == 2:
            close_date, _, original_amount = line.split()
        if index == 3:
            actual_amount, interest = line.split()

        close_date = format_date(close_date)
        open_date = format_date(open_date)
        original_amount = format_won(original_amount)
        actual_amount = format_won(actual_amount)
        interest = format_won(interest)

        index += 1

        if index == lines_per_record:
            index = 0
            print(
                title,
                account_number,
                open_date,
                original_amount,
                actual_amount,
                interest,
            )
            account = Account(
                account_number=account_number,
                description=title,
                bank=mg,
                open_date=open_date,
                close_date=close_date,
                is_active=False,
            )
            account.save()
