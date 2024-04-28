from flask import Flask, session
from routes import home, budget, register, login, logout, buy_flag
from utils import init_db
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

init_db()

app.add_url_rule('/', view_func=home)
app.add_url_rule('/budget', view_func=budget, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout)
app.add_url_rule('/buy_flag', view_func=buy_flag, methods=['POST'])

if __name__ == '__main__':
    app.run()
