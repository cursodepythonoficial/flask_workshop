from flask import Flask

app = Flask(__name__)
app.config.from_json('settings.json')

@app.route("/")
def home():
    return "hello world"

@app.route("/hello/<name>")
def hello(name):
    return f"hello {name}"

app.run(use_reloader=True)
