from utils import add_income, add_expense, add_saving
from datetime import datetime

options = ['Income', 'Expense', 'Saving']

incomes = []
expenses = []
savings = []

def add_register(options):
    while True:
        print("What do you want to add?")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        
        choice = input("Enter your choice (1-{0}): ".format(len(options)))

        if choice == '1':
            name = input("Name: ").capitalize()
            amount = float(input("Amount: "))
            currency = input("Currency: ").upper()
            category = input("Category: ").capitalize()
            account = input("Account: ").capitalize()
            
            if input("Was it made it today? [Y/N]: ").upper() =='N':
                date = datetime.strptime(input("Date (YYYY-MM-DD): "), "%Y-%m-%d")
            else:
                date = datetime.now()
            
            args = [name, amount, category, account, currency, date]
            
            try:
                income = add_income(*args)
                incomes.append(income)
                print(f"Income {income.name} for ${income.amount} succesfully registered.")
            except Exception as e:
                print(f"Error while registering Income: {e}. Try again")

        elif choice == '2':
            name = input("Name: ").capitalize()
            amount = float(input("Amount: "))
            category = input("Category: ").capitalize()
            account = input("Paid with: ").upper()
            currency = input("Currency: ").upper()
            
            if input("Was it made today? [Y/N] ").upper() =='N':
                date = datetime.strptime(input("Date (YYYY-MM-DD): "), "%Y-%m-%d")
            else:
                date = datetime.now()
            
            if input("Expense Type (Credit, Debit): ").capitalize() == 'Credit':
                installments = int(input("In how many installments?: "))
                is_credit=True
            else:
                is_credit, installments= False, 0
            
            if input("Has been paid? [Y/N]: ") == 'N':
                status='Pending'
            else:
                status='Paid'
            
            args = [name, amount, is_credit, installments, date, category, currency, account, status]

            try:
                expense = add_expense(*args)
                expenses.append(expense)
                print(f"Expense {expense.name} for ${expense.amount} succesfully registered.")
            except Exception as e:
                print(f"Error while registering Expense: {e}. Try again")
            
        if choice == '3':
            name = input("Name: ").capitalize()
            amount = float(input("Amount: "))
            category = input("Category: ").capitalize()
            currency = input("Currency: ").upper()
            if input("Was it made today? [Y/N]: ").upper() =='N':
                date = datetime.strptime(input("Date (YYYY-MM-DD): "), "%Y-%m-%d")
            else:
                date = datetime.now()
            
            args = [name, amount, category, currency, date]

            try:
                saving = add_saving(*args)
                savings.append(saving)
                print(f"Saving {saving.name} for ${saving.amount} succesfully registered.")
            except Exception as e:
                print(f"Error while registering Saving: {e}. Try again")
            
        if input("Do you want to add more registers? [Y/N]: ").upper() != 'Y':
            break

if __name__ == '__main__':
    add_register(options)
    
    print("\nSummary: ")
    print("Income Count: ", len(incomes))
    print("Expense Count: ", len(expenses))
    print("Saving Count: ", len(savings))

