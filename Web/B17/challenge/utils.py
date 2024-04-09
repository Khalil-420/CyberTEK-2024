import sqlite3

def init_db():
    conn = sqlite3.connect('budget.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    budget REAL
                 )''')
    conn.commit()
    conn.close()

    conn = sqlite3.connect('budget.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    travel REAL DEFAULT 0,
                    food REAL DEFAULT 0,
                    entertainment REAL DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                 )''')
    conn.commit()
    conn.close()
