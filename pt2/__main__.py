from flask import Flask, jsonify, Response, render_template, Markup

app = Flask(__name__)
app.config['DEBUG'] = False


# Views should return a Response object
@app.route('/')
def response():
    return Response("Hello Response", status=200, headers={'foo': 'bar'})


# Return string to get automatic Response with status_code 200 Ok
@app.route("/auto")
def home():
    return "Automatic Response"


# return a tuple of "string", status_code to specify it
@app.route("/status")
def hello():
    return "Status Code", 200


# return a tuple of "string", status_code, headers
@app.route("/headers")
def world():
    return "Headers", 201, {'Content-Type': 'text', 'mytag': 'foo'}


# JSON should be jsonified
@app.route('/json')
def json():
    data = {'data': {'a': 'b'}}
    #return str(data)
    return jsonify(data)


# html text surrounded by Markup
@app.route('/tags')
def tags():
    return Markup("<ul><li>Hello</li><li>World</li></ul>")


# or template rendered
@app.route('/template')
def template():
    return render_template('template.html', msg="Hello Grupy")


app.run(use_reloader=True)
