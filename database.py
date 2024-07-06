import sqlite3

def create_database(database):
    """Connect to SQLite database and print the version."""
    conn = None
    try:
        conn = sqlite3.connect(database)
        print(f'Database version: {sqlite3.sqlite_version}')
    except sqlite3.Error as e:
        print(f'Error connecting to {database}: {e}')
    finally:
        if conn:
            conn.close()

def create_tables(database):
    """Create tables in the SQLite database if they do not exist."""
    sql_statements = [
        """CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            amount NUMERIC NOT NULL,
            is_credit INTEGER NOT NULL,
            installments INTEGER NOT NULL,
            installments_amount NUMERIC,
            installments_dates TEXT,
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
        with sqlite3.connect(database) as conn:
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

if __name__ == '__main__':
    database_name = "data.db"
    create_database(database_name)
    create_tables(database_name)