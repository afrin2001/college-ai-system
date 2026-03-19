import sqlite3
import os

DB_PATH = "../database/students.db"

def init_db():
    os.makedirs("../database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password TEXT
    )''')

    conn.commit()
    conn.close()

def add_student(name, email, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO students (name,email,password) VALUES (?,?,?)",
              (name, email, password))
    conn.commit()
    conn.close()

def validate_user(email, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE email=? AND password=?",
              (email, password))
    user = c.fetchone()
    conn.close()
    return user
