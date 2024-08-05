import sqlite3
from fastapi import HTTPException

def get_db(DATABASE):
    conn = sqlite3.connect(DATABASE)
    return conn

def create_record(db: str, table: str, fields: tuple, values: tuple):
    conn = get_db(db)
    cursor = conn.cursor()
    placeholders = ', '.join(['?'] * len(values))
    query = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({placeholders})"
    try:
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()
    return {"message": f"Record successfully added to {table}."}

def delete_record(db: str, table: str, id: int):
    conn = get_db(db)
    cursor = conn.cursor()
    query = f"DELETE FROM {table} WHERE id={id}"
    try:
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()
    return {"message": f"Record successfully deleted from {table}"}
