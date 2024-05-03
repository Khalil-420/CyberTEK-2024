from flask import Flask, request, render_template, redirect, url_for, session
from db import connect_db,generate_random_string,add_user, query_user_profile, update_username, update_password,update_description, add_note,verify_user,getnotes,query_special,create_tables,add_admins
import os

app = Flask(__name__)
app.secret_key = generate_random_string(80)
FLAG = os.environ['FLAG']

create_tables()
add_admins(FLAG)

# Routes
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        description = request.form['description'] 
                
        if verify_user(username):
            return 'Username already exists. Please choose another username.'
        
        add_user(username, password, description,0)
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('profile'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = verify_user(username)
        if user and user[2] == password:
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('profile'))
        else:
            return 'Invalid username or password'
    
    return render_template('login.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    
    if request.method == 'POST':
        if 'username' in request.form and request.form['username'].strip():
            new_username = request.form['username']
            update_username(user_id, new_username)
        
        if 'password' in request.form and request.form['password'].strip():
            new_password = request.form['password']
            update_password(user_id, new_password)

        if 'description' in request.form and request.form['description'].strip():
            new_description = request.form['description']
            update_description(user_id, new_description)   
        
        if 'note' in request.form and request.form['note'].strip():
            note = request.form['note']
            add_note(user_id, note)
        
        return redirect(url_for('profile'))
    
    user_profile = query_user_profile(user_id)
    print(user_profile)
    notes = getnotes(user_id)
    special_users = sorted(query_special(user_id), key=lambda x: (x[1], x[3] if x[1] == user_profile[1] and x[3] != user_profile[3] else x[2]))
    
    return render_template('profile.html', user_profile=user_profile, notes=notes, admins=special_users)

if __name__ == '__main__':
    app.run()
