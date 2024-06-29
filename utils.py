from money import Expense, Income, Saving, Account

def add_income(name, amount, category, account, currency, date):
    income = Income(
        name=name,
        amount=amount,
        category=category,
        account=account,
        currency=currency,
        date=date
    )
    return income


def add_expense(name, amount, is_credit, installments, date, category, currency, account, status):
    expense = Expense(
        name=name,
        amount=amount,
        is_credit=is_credit,
        installments=installments,
        date=date,
        category=category,
        currency=currency,
        account=account,
        status=status
    )
    return expense

def add_saving(name, amount, category, currency, date):
    saving = Saving(
        name=name,
        amount=amount,
        category=category,
        currency=currency,
        date=date
    )
    return saving

def add_account(name, description, type):
    account = Account(
        name=name,
        description=description,
        type=type
    )
    return account