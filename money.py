from datetime import datetime, timedelta

class Expense:
    def __init__(self,
                name: str,
                amount: float,
                is_credit: bool,
                installments: int,
                date: datetime,
                category: str,
                currency: str,
                paid_with: str,
                status: str
                ):
        self.name = name
        self.amount = amount
        self.is_credit = is_credit
        self.installments = installments
        self.date = date
        self.category = category
        self.currency = currency
        self.paid_with = paid_with
        self.status = status

        if self.is_credit:
            self.installment_amount = self.amount / self.installments
        else:
            self.installment_amount = None

        self.installment_dates = self.calculate_installments_dates()

    def calculate_installments_dates(self):
        installment_dates = []
        if self.is_credit:
            for _ in range(1, self.installments + 1):
                due_month = (self.date.month + 1) % 12
                due_year = self.date.year + (self.date.month + 1) // 12
                due_date = datetime(due_year, due_month, 1)
                installment_dates.append(due_date)
        return installment_dates
            
class Income:
    def __init__(self,
                name: str,
                amount: float,
                category: str,
                account: str,
                currency: str,
                date: datetime
                ):
        self.name = name
        self.amount = amount
        self.category = category
        self.account = account
        self.currency = currency
        self.date = date
class Saving:
    def __init__(self,
                name: str,
                amount: float,
                category: str,
                currency: str,
                date: datetime
                ):
        self.name = name
        self.amount = amount
        self.category = category
        self.currency = currency
        self.date = date
