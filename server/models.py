from datetime import datetime, timedelta
from pydantic import BaseModel
from typing import Optional, List

class Account(BaseModel):
    name: str
    description: str
    type: str

class Money(BaseModel):
    name: str
    date: datetime
    amount: float
    account: int
    category: str
    currency: str

class Expense(Money):
    is_credit: bool
    installments: Optional[int] = None
    status: str
    
    def calculate_installments_amount(self) -> Optional[float]:
        if self.installments and self.installments > 0:
            return self.amount / self.installments
        return None
    
    def calculate_installments_dates(self) -> Optional[List[datetime]]:
        if self.installments and self.installments > 0:
            return [self.date + timedelta(days=30 * i) for i in range(self.installments)]
        return None
            
class Income(Money):
    pass
    
class Saving(Money):
    pass