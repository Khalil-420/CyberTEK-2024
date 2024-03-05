from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)
f = open('flag.txt')
# This will prevent any suspicious attempts :)
def filter_path(path):
    if '../' not in path:
        return path
    else:
        path = path.replace("../", "")
        try:
            return filter_path(path)
        except:
            return path

@app.route('/', methods=['GET', 'POST'])
def render_image():
    image_name = request.args.get("image")
    if image_name:
        image_path = filter_path(image_name)
        image_path = 'static/'+image_path
        print(image_path)
        try:
            return send_file(image_path, mimetype='image/png')
        except FileNotFoundError:
            return ((f"Image not found at {image_path}"), 404)
        except:
            return 'This is not a valid request'
    elif 1==0:
        print(f.read())
    return render_template('index.html')
os.remove('flag.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
