from fastapi import FastAPI
import sqlite3
app = FastAPI()

DATABASE = 'data.db'

def connect_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def get_all_records(query):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return records

def execute_query(query, params):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

@app.get("/incomes")
def get_incomes():
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
def get_expenses():
    query = "SELECT * FROM expenses"
    records = get_all_records(query)
    formatted_records = []
    for record in get_all_records(query):
        formatted_record = {
            "id": record[0],
            "name": record[1],
            "amount": record[2],
            "is_credit": record[3],
            "installments": record[4],
            "date": record[5],
            "category": record[6],
            "currency": record[7],
            "account_id": record[8],
            "status": record[9]
        }
        formatted_records.append(formatted_record)
    return {"expenses": formatted_records}

@app.get("/savings")
def get_savings():
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
def get_accounts():
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
def get_account_details(id: int):
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