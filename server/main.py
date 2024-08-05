from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from utils import get_db, create_record, delete_record
from models import Account, Expense, Income, Saving

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
DATABASE = 'data.db'

def get_all_records(query):
    conn = get_db(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return records

def execute_query(query, params):
    conn = get_db(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

@app.get("/incomes")
async def get_incomes():
    query = "SELECT * FROM incomes"
    formatted_records = []
    for record in get_all_records(query):
        formatted_record = {
            "id": record[0],
            "name": record[1],
            "amount": record[2],
            "category": record[3],
            "currency": record[4],
            "date": record[5],
            "account": record[6]
        }
        formatted_records.append(formatted_record)

    return {"incomes": formatted_records}

@app.get("/expenses")
async def get_expenses():
    query = "SELECT * FROM expenses"
    formatted_records = []
    for record in get_all_records(query):
        formatted_record = {
            "id": record[0],
            "name": record[1],
            "amount": record[2],
            "is_credit": record[3],
            "installments": record[4],
            "installments_amount": record[5],
            "installments_dates": record[6],
            "date": record[7],
            "category": record[8],
            "currency": record[9],
            "account_id": record[10],
            "status": record[11]
        }
        formatted_records.append(formatted_record)
    return {"expenses": formatted_records}

@app.get("/savings")
async def get_savings():
    query = "SELECT * FROM savings"
    formatted_records = []
    for record in get_all_records(query):
        formatted_record = {
            "id": record[0],
            "name": record[1],
            "amount": record[2],
            "category": record[3],
            "currency": record[4],
            "date": record[5],
            "account": record[6]
        }
        formatted_records.append(formatted_record)

    return {"savings": formatted_record}

@app.get('/accounts')
async def get_accounts():
    query = f"SELECT * FROM accounts"
    formatted_records = []
    for record in get_all_records(query):
        formatted_record = {
            "id": record[0],
            "name": record[1],
            "description": record[2],
            "type": record[3],
        }
        formatted_records.append(formatted_record)
    return {"accounts": formatted_records}

@app.get("/accounts/{id}")
async def get_account_details(id: int):
    query = f"SELECT * FROM accounts WHERE id={id}"
    formatted_records = []
    for record in get_all_records(query):
        formatted_record = {
            "id": record[0],
            "name": record[1],
            "description": record[2],
            "type": record[3],
        }
        formatted_records.append(formatted_record)
    return {"account_details": formatted_records}

@app.post("/incomes/")
async def create_income(income: Income):
    return create_record(DATABASE,
                        'incomes',
                        ('name', 'date', 'amount', 'account_id', 'category', 'currency'),
                        (income.name, income.date, income.amount, income.account, income.category, income.currency))

@app.post("/expenses/")
async def create_expense(expense: Expense):
    return create_record(DATABASE,
                        'expenses',
                        ('name', 'date', 'amount', 'account_id', 'category', 'currency', 'is_credit', 'installments', 'status'),
                        (expense.name, expense.date, expense.amount, expense.account, expense.category, expense.currency, expense.is_credit, expense.installments,expense.status))

@app.post("/savings/")
async def create_saving(saving: Saving):
    return create_record(DATABASE,
                        'savings',
                        ('name', 'date', 'amount', 'account_id', 'category', 'currency'),
                        (saving.name, saving.date, saving.amount, saving.account,saving.category, saving.currency))

@app.post("/accounts/")
async def create_account(account: Account):
    return create_record(DATABASE,
                        'accounts',
                        ('name', 'description', 'type'),
                        (account.name, account.description, account.type))

@app.delete("/accounts/{id}")
async def delete_account(id: int):
    return delete_record(DATABASE,
                        'accounts',
                        id)

@app.delete("/incomes/{id}")
async def delete_income(id: int):
    return delete_record(DATABASE,
                        'incomes',
                        id)


@app.delete("/savings/{id}")
async def delete_saving(id: int):
    return delete_record(DATABASE,
                        'savings',
                        id)

@app.delete("/expenses/{id}")
async def delete_expense(id: int):
    return delete_record(DATABASE,
                        'expenses',
                        id)
