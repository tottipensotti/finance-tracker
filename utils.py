from money import Expense, Income, Saving
from datetime import datetime

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


def add_expense(name, amount, is_credit, installments, date, category, currency, paid_with, status):
    expense = Expense(
        name=name,
        amount=amount,
        is_credit=is_credit,
        installments=installments,
        date=date,
        category=category,
        currency=currency,
        paid_with=paid_with,
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