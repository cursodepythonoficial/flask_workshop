from flask import Flask, render_template, abort

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def template():
    return "Hello World"

# what happens if localhost:5000/sfdfsdfsdf is requested?
# take a look in app2.py
