from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route("/")
def home():
    # bla # uncomment to generate error
    return "Hello World"


if __name__ == "__main__":
    app.run(use_reloader=True)
