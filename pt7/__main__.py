from flask import Flask
from functions import upperfy

app = Flask(__name__)
app.config.from_json('settings.json')

@app.route("/")
def home():
    return "hello world"

@app.route("/hello/<name>")
def hello(name):
    return f"hello {name}"


app.add_url_rule(
    rule="/upperfy/<text>",
    view_func=upperfy
)

app.run(use_reloader=True)
