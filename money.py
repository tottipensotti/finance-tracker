from datetime import datetime, timedelta

class Expense:
    def __init__(self,
                name: str,
                amount: float,
                is_credit: bool,
                installments: int,
                timestamp: datetime,
                category: str,
                status: str,
                paid_with: str
                ):
        self.timestamp = timestamp
        self.name = name
        self.paid_with = paid_with
        self.category = category
        self.is_credit = is_credit
        self.installments = installments
        self.amount = amount
        self.status = status

        if self.is_credit:
            self.installment_amount = self.amount / self.installments
        else:
            self.installment_amount = None

        self.installment_dates = self.calculate_installments_dates()

    def calculate_installments_dates(self):
        installment_dates = []
        if self.is_credit:
            for i in range(1, self.installments + 1):
                due_month = (self.timestamp.month + 1) % 12
                due_year = self.timestamp.year + (self.timestamp.month + 1) // 12
                due_date = datetime(due_year, due_month, 1)
                installment_dates.append(due_date)
        return installment_dates
            
class Income:
    def __init__(self,
                name: str,
                amount: float,
                timestamp: datetime,
                type: str,
                account: str
                ):
        self.timestamp = timestamp
        self.name = name
        self.account = account
        self.type = type
        self.amount = amount
class Savings:
    def __init__(self,
                name: str,
                amount: float,
                timestamp: datetime,
                category: str):
        self.name = name
        self.amount = amount
        self.timestamp = timestamp
        self.category = category
