import sqlite3

def create_database(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        print(f'Database version: {sqlite3.sqlite_version}')
    except sqlite3.Error as e:
        print(f'Error connecting to ${database}: {e}')
    finally:
        if conn:
            conn.close()

def create_tables():
    sql_statements = [
        """CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            amount NUMERIC NOT NULL,
            is_credit INTEGER NOT NULL,
            installments INTEGER NOT NULL,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            currency TEXT NOT NULL,
            account_id INT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (account_id) REFERENCES accounts(id)
        );""",
        """CREATE TABLE IF NOT EXISTS incomes (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            amount NUMERIC NOT NULL,
            category TEXT NOT NULL,
            currency TEXT NOT NULL,
            date TEXT NOT NULL,
            account_id INT NOT NULL,
            FOREIGN KEY (account_id) REFERENCES accounts(id)
        );""",
        """CREATE TABLE IF NOT EXISTS savings (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            amount NUMERIC NOT NULL,
            category TEXT NOT NULL,
            currency TEXT NOT NULL,
            date TEXT NOT NULL,
            account_id INT NOT NULL,
            FOREIGN KEY (account_id) REFERENCES accounts(id)
        );""",
        """CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            type TEXT NOT NULL
        );"""
    ]
    
    try:
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)            
            conn.commit()
            cursor.execute("""
                SELECT name
                FROM sqlite_schema
                WHERE type ='table'
                    AND name NOT LIKE 'sqlite_%';"""
            )
            print(cursor.fetchall())
    except sqlite3.Error as e:
        print(e)


def add_expense(conn, expense):
    sql="""
        INSERT INTO expenses(name, amount, is_credit, installments, date, 
                            category, currency, account_id, status)
        VALUES(?,?,?,?,?,?,?,?,?)
    """
    cur = conn.cursor()
    cur.execute(sql, expense)
    conn.commit()
    return cur.lastrowid

def add_income(conn, income):
    sql="""
        INSERT INTO incomes(name,amount,category,currency,date,account_id)
        VALUES(?,?,?,?,?,?)
    """
    cur = conn.cursor()
    cur.execute(sql, income)
    conn.commit()
    return cur.lastrowid

def add_saving(conn, saving):
    sql="""
        INSERT INTO savings(name,amount,category,currency,date,account_id)
        VALUES(?,?,?,?,?,?)
    """
    cur = conn.cursor()
    cur.execute(sql, saving)
    conn.commit()
    return cur.lastrowid

def add_account(conn, account):
    sql="""
        INSERT INTO accounts(name, description, type)
        VALUES(?,?,?)
    """
    cur = conn.cursor()
    cur.execute(sql, account)
    conn.commit()
    return cur.lastrowid

def insert_rows():
    try:
        with sqlite3.connect('data.db') as conn:
            account = ('Test', 'Test Account', 'Test')
            account_id = add_account(conn, account)
            
            expense = ('Test', 1500, 0, 0, '2024-06-23 21:47:13.000', 
                            'Test', 'USD', account_id, 'Paid')
            expense_id = add_expense(conn, expense)
            
            income = ('Test',1000,'Test','USD','2024-06-23 21:47:13.000',account_id)
            income_id = add_income(conn, income)
            
            saving = ('Test', 5000, 'Test', 'USD', '2024-06-23 21:47:13.000', account_id)
            saving_id = add_saving(conn, saving)
            
            print(f'Created an account with the id {account_id}')
            print(f'Created a saving with the id {saving_id}')
            print(f'Created an expense with the id {expense_id}')
            print(f'Created an income with the id {income_id}')

            sql_statements = [
                "SELECT * FROM accounts;",
                "SELECT * FROM expenses;",
                "SELECT * FROM incomes;",
                "SELECT * FROM savings;"
            ]
            cur = conn.cursor()
            for statement in sql_statements:
                cur.execute(statement)
                print(cur.fetchall())
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    create_database("data.db")
    create_tables()
    insert_rows()