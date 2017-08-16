from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/hello/<name>')
def hello1(name):
    return f'Hello {name}'


@app.route('/hello2/<string:name>')
def hello2(name):
    return f'Hello {name}'


@app.route('/soma/<int:x>/<int:y>')
def soma(x, y):
    return f'The result is: {x + y}'


@app.route('/soma2/<float:x>/<float:y>')
def soma2(x, y):
    return f'The result is: {x + y}'


@app.route('/path/<path:filepath>')
def path1(filepath):
    return f'Location is {filepath}'

# prefixes

@app.route('/home/@<username>')  # <- catch `@` prefixed
def user_profile(username):
    return f"This is {username}'s profile page."

# suffixes

@app.route('/<path:path>.php')  # <- catch `.php` suffixed
def not_php(path):
    return f"I am not really php! :)"

@app.route('/<path:path>.<string:ext>')  # <- catch `.*` suffixed
def not_ext(path, ext):
    return f"I am not really {ext}! :)"

# multiple routes single view

@app.route('/home/')
@app.route('/home/<name>')
@app.route('/home/<name>/<int:number>')
@app.route('/home/<name>/<float:number>')
@app.route('/home/<path:name>')  # <- catch all
def multiple(name=None, number=None):
    return f'Hello {name or "Bruno"} - {number or 42}'


# app.url_map.converter = CustomConverter

# trailing /

@app.route('/resource')
def resource():
    return "This is not returned for /resource/ only /resource"


@app.route('/trailing/')
def trailing():
    return "This is not returned for /trailing/ and /trailing is a redirect"
