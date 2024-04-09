from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import random
import time
import base64
from hashlib import sha256
from datetime import datetime
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(64)

FLAG = "Securinets{N0T_S0_R4ND0M_4FT3R_4LL!}"

def get_quote(champion):
    try:
        if ".." in champion:
            raise Exception("Nope!")
        quote_file = os.path.join('quotes', champion)
        with open(quote_file, 'r') as file:
            quotes = file.readlines()
        return random.choice(quotes)
    except Exception as e:
        # print(e)
        return False

def generated_pwd_hash(n=128):
    random.seed(int(time.time()))
    generated_pwd = random.getrandbits(n)
    generated_pwd_hash = sha256(bytes.fromhex(hex(generated_pwd)[2:].rjust(32,'0'))).hexdigest()
    return generated_pwd_hash

def verify_pwd(pwd, stored_hash):
    pwd_hash = sha256(bytes.fromhex(hex(int(pwd))[2:])).hexdigest()
    return pwd_hash == stored_hash

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password_hash TEXT,
                    created_at DATE DEFAULT CURRENT_DATE
                 )''')

    c.execute('SELECT * FROM users')
    users = c.fetchone()
    if not users: 
        initial_users = [
            ('Jinx', generated_pwd_hash(), datetime.now().date()),
            ('Caitlyn', generated_pwd_hash(), datetime.now().date()),
            ('Viktor', generated_pwd_hash(), datetime.now().date()),
            ('Jayce', generated_pwd_hash(), datetime.now().date())
        ]
        c.executemany('INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)', initial_users)
        conn.commit()

    conn.close()

def backup():
    conn = sqlite3.connect('users.db')
    c=conn.cursor()
    c.execute('SELECT * FROM users')

    users = c.fetchall()
    c.close()
    conn.close()
    with open('backup.txt', 'w') as file:
        for user in users:
            file.write(str(user) + '\n')

init_db()
backup()    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM users WHERE username = ?''', (username,))
        user = c.fetchone()
        conn.close()

        if user and verify_pwd(password, user[2]):
            session['username'] = username
            return redirect(url_for('flag'))
        else:
            return "Invalid username or password. Please try again."

    return render_template('login.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quote/<champion>')
def quote(champion):
    try:
        champion = base64.b64decode(champion.encode()).decode()
        quote = get_quote(champion)
        if quote:
            return render_template('quote.html', champion=champion, quote=quote)
        else:
            return "Champion doesn't exist!"
    except:
        return "Champion doesn't exist! Error"

@app.route('/flag')
def flag():
    if 'username' in session:
        return f"Welcome to Summoners Rift! {FLAG}"
    else:
        return "You're not logged in"

if __name__ == '__main__':
    app.run()
