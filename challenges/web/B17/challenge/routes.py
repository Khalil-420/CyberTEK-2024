from flask import render_template, request, redirect, url_for, session
import sqlite3,os

FLAG = os.environ['FLAG']

def home():
    return render_template('home.html')

def budget():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect('budget.db')
    c = conn.cursor()

    c.execute('''SELECT budget FROM users WHERE username = ?''', (session['username'],))
    user_budget = c.fetchone()[0]

    if request.method == 'POST':
        travel = float(request.form['travel'])
        food = float(request.form['food'])
        entertainment = float(request.form['entertainment'])

        c.execute('''SELECT travel,food,entertainment FROM expenses WHERE user_id = ?''', (session['user_id'],))
        existing_expenses = c.fetchone()

        total_expense = travel + food + entertainment
        if total_expense > user_budget:
            error_message="Total expense cannot exceed your budget."
            if existing_expenses:
                return render_template('budget.html',user_budget=user_budget,travel_expense = existing_expenses[0],food_expense=existing_expenses[1],entertainment_expense=existing_expenses[2],error=error_message)
            else:
                return render_template('budget.html',user_budget=user_budget,error=error_message)
        if existing_expenses: 
            travel_expense = existing_expenses[0] + travel
            food_expense = existing_expenses[1] + food
            entertainment_expense = existing_expenses[2] + entertainment

            c.execute('''UPDATE expenses SET travel = ?, food = ?, entertainment = ? WHERE user_id = ?''',
                      (travel_expense, food_expense, entertainment_expense, session['user_id']))
        else: 
            c.execute('''INSERT INTO expenses (user_id, travel, food, entertainment) VALUES (?, ?, ?, ?)''',
                      (session['user_id'], travel, food, entertainment))
        conn.commit()
        c.execute('''UPDATE users SET budget = ? WHERE username = ?''',
                      (user_budget-(travel+food+entertainment), session['username']))
        conn.commit()
        return redirect(url_for('budget'))

    c.execute('''SELECT travel,food,entertainment FROM expenses WHERE user_id = ?''', (session['user_id'],))
    expenses_row = c.fetchone()

    travel_expense = float(expenses_row[0]) if expenses_row else 0
    food_expense = float(expenses_row[1]) if expenses_row else 0
    entertainment_expense = float(expenses_row[2]) if expenses_row else 0

    total_expense = travel_expense + food_expense + entertainment_expense

    conn.close()

    return render_template('budget.html', user_budget=user_budget, travel_expense=travel_expense,
                           food_expense=food_expense, entertainment_expense=entertainment_expense)


def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(password) < 10 :
            error_message="Please use a password length superior than 10!" 
            return render_template('register.html',error=error_message)
        conn = sqlite3.connect('budget.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM users WHERE username = ?''', (username,))
        if c.fetchone():
            error_message="Username already exists. Please choose a different one."
            return render_template('register.html',error=error_message)

        c.execute('''INSERT INTO users (username, password, budget) VALUES (?, ?, ?)''', (username, password, 1000))

        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('budget.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = username
            session['user_id'] = user[0]
            return redirect(url_for('budget'))
        else:
            error_message="Invalid username or password. Please try again."
            return render_template('login.html',error=error_message)

    return render_template('login.html')

def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('home'))

def buy_flag():
    conn = sqlite3.connect('budget.db')
    c = conn.cursor()

    c.execute('''SELECT travel,food,entertainment FROM expenses WHERE user_id = ?''', (session['user_id'],))
    expenses = c.fetchone()
    c.execute('''SELECT budget FROM users WHERE username = ?''', (session['username'],))
    user_budget = c.fetchone()[0]

    if user_budget >= 0:
        if expenses[0] == 1337 and expenses[1] == 1337 and expenses[2] == 1337:
            return render_template('budget.html', user_budget=user_budget, message=FLAG)
        else:
            error_message = "Not enough!"
            return render_template('budget.html', user_budget=user_budget, travel_expense=expenses[0],
                           food_expense=expenses[1], entertainment_expense=expenses[2],error=error_message)
    else:
        error_message = "Something Odd is happening!"
        return render_template('budget.html', user_budget=user_budget, travel_expense=expenses[0],
                           food_expense=expenses[1], entertainment_expense=expenses[2],error=error_message)
