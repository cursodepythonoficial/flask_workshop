from flask import Flask

class Grupysk(Flask):
    def make_response(self, rv):
        if isinstance(rv, str):
            rv = rv.upper()
        return super(Grupysk, self).make_response(rv)

app = Grupysk(__name__)
app.config['DEBUG'] = False

@app.route("/")
def home():
    return "hello world"

@app.route("/hello/<name>")
def hello(name):
    return f"hello {name}"

app.run(use_reloader=True)
