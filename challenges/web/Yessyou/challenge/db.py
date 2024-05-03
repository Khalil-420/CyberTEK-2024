import sqlite3
import random
import string
import os


def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def connect_db():
    return sqlite3.connect('yessyou.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            description TEXT,
            is_admin INTEGER DEFAULT 0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            note TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')


    conn.commit()
    conn.close()

def add_user(username, password, description,is_admin):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, description,is_admin) VALUES (?, ?, ?, ?)', (username, password, description,is_admin))
    conn.commit()
    conn.close()

def verify_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user


def query_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def update_username(user_id, new_username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET username = ? WHERE id = ?', (new_username, user_id))
    conn.commit()
    conn.close()

def update_password(user_id, new_password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET password = ? WHERE id = ?', (new_password, user_id))
    conn.commit()
    conn.close()

def update_description(user_id,new_description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET description = ? WHERE id = ?', (new_description, user_id))
    conn.commit()
    conn.close()

def add_note(user_id, note):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (user_id, note) VALUES (?, ?)', (user_id, note))
    conn.commit()
    conn.close()

def query_user_profile(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user_profile = cursor.fetchone()
    conn.close()
    return user_profile

def getnotes(id):
    the_notes = []
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT note from notes where user_id = ?",(id,))
    notes = cursor.fetchall()
    conn.close()
    for i in range(len(notes)):
        the_notes.append(notes[i][0])
    print(the_notes)
    return the_notes

def query_special(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * from users where is_admin=1")
    admins = cursor.fetchall()
    admins.append(query_user_profile(id))
    conn.close()
    return admins

def add_admins(FLAG):
    add_user("Yasuo",FLAG,"Virtue is no more than a luxury.",1)
    add_user("Vi",generate_random_string(60),"If I want your opinion, I'll beat it out of you.",1)
