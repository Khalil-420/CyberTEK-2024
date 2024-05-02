import mimetypes
import os
import random
import shutil
import string
from sys import stderr
import glob
import requests
from flask import Flask, render_template, render_template_string, request
from flask_caching import Cache

cache = Cache(config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': './static/cache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_THRESHOLD': 500
})
app = Flask(__name__, static_url_path='/static', static_folder='static')
cache.init_app(app)

app.config['UPLOAD_FOLDER'] = './uploads'

# you don't need these if you really want to show your love for psyduck...
NOPE = ['config', 'namespace', 'joiner', 'class', 'subclasses', 'list', 'last', '{{', '}}', 'getitem',
        '[', ']', '\'', '"', '+', '/', '$', 'format', 'attr', 'attribute', 'select', 'safe', 'items',
        'read', 'globals', 'init', 'request', '.', '?', '\\x', 'select', 'decode', 'hex', 'base64',
        'float', 'string', 'ls', 'os', 'flag', 'cat', 'id']


def secure(fact_value: str):
    for bad in NOPE:
        if bad in fact_value:
            print(bad, file=stderr, flush=True)
            return "that's not love.."
    return fact_value


def admin(req):
    return req.remote_addr in ['127.0.0.1']

def health():
    folders = glob.glob("uploads/*")
    if len(folders)>0:
        for folder in folders:
            id = folder.split('/')[1]
            requests.get(f'http://127.0.0.1:1337/fact/{id}')
    return True

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method != 'POST':  
        health()
        return render_template('index.html', status='')

    
    fact_value = secure(request.form.get('fact'))
    img = request.files['file']
    if len(fact_value) > 2000:
        return render_template('index.html', status="that's not love..")

    if not fact_value or not img:
        return render_template('index.html', status='Something went wrong..')

    fact_id = ''.join(random.choice(string.ascii_letters) for _ in range(32))
    upload_path = f'{app.config["UPLOAD_FOLDER"]}/{fact_id}'
    try:
        os.mkdir(upload_path)
        file_path = f'{app.config["UPLOAD_FOLDER"]}/{fact_id}/{fact_id}'
        file_mimetype = img.content_type
        extension = mimetypes.guess_extension(file_mimetype)
        if not extension:
            extension = ''

        with open(f'{file_path}.txt', 'w') as f:
            f.write(fact_value)

        img.save(f'./static/imgs/{fact_id}{extension}')

        return render_template('index.html',
                               status=f'Your love for psyduck have been submitted under id: {fact_id}! Thanks for '
                                      'the love :D')
    except OSError:
        return render_template('index.html', status='Something went wrong..')


@app.route('/fact/<fact_id>', methods=['GET'])
@cache.cached(timeout=50)
def fact(fact_id: str):
    # only admins can check your submissions for now.
    if not admin(request):
        return render_template(
            'fact.html',
            out='Something went wrong..',
            img='static/imgs/internal/sadpsy.jpg'
        ), 500

    path = f'{app.config["UPLOAD_FOLDER"]}/{fact_id}'
    if not os.path.isdir(path):
        return render_template(
            'fact.html',
            out='Not found :/',
            img='static/imgs/internal/sadpsy.jpg'
        )

    try:
        fact_value = open(f'{path}/{fact_id}.txt').read()
        shutil.rmtree(path, ignore_errors=True)
    except OSError:
        fact_value = 'none'

    return render_template(
        'fact.html',
        out=render_template_string(fact_value),
        img=f'{fact_id}'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=False)
