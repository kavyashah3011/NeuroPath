import sqlite3
import json

DB_NAME = "resume_data.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_resume(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO resumes (data) VALUES (?)",
        (json.dumps(data),)
    )

    conn.commit()
    conn.close()