from flask import Flask, request, send_file
from os import listdir, path

app = Flask(__name__)

def ls(q):
    if path.isdir(q):
        return [f for f in listdir(q) if not f.startswith('.')]
    
    return []

def cat(q):
    if path.isfile(q):
        with open(q, 'rb') as f:
            return f.read()
    
    return b""

@app.get("/ls")
def list():
    q = request.args.get('q') or '.'
    if q.startswith("/"):
        q = q.replace("/","")
    elif q.startswith(".."):
        q = q.replace("..","")
    elif q.startswith("."):
        q = q.replace(".","")
    return ls(q)

@app.get("/cat")
def read():
    q = request.args.get('q')
    if q.startswith("/"):
        q = q.replace("/","")
    elif q.startswith(".."):
        q = q.replace("..","")
    elif q.startswith("."):
        q = q.replace(".","")
    return cat(q)

@app.get("/")
def code():
    return send_file(__file__)


@app.errorhandler(Exception)
def all_exception_handler(error):
    return str(error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=False)