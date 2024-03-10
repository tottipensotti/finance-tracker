from money import Expense
from datetime import datetime

# Example of an Expense
expense = Expense(
    name="Test",
    amount = 120000.0,
    is_credit = True,
    installments = 12,
    timestamp = datetime(2024,1,30),
    category = "Test",
    status = "Pending",
    paid_with = "Visa Credit Card"
)

if __name__ == "__main__":
    print("Expense Details:")
    print("Name:", expense.name)
    print("Amount:", expense.amount)
    print("Is Credit:", expense.is_credit)
    print("Installments:", expense.installments)
    print("Timestamp:", expense.timestamp)
    print("Category:", expense.category)
    print("Status:", expense.status)
    print("Paid With:", expense.paid_with)
    print("Installment Amount:", expense.installment_amount)
    print("Installment Dates:")
    for i, date in enumerate(expense.installment_dates, 1):
        print("Installment", i, ":", date)
