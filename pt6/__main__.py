import os
import yaml
from flask import Flask, Config

class MyConfig(Config):
    def from_yaml(self, path):
        curdir = os.path.dirname(os.path.abspath(__file__))
        config_dict = {
            key.upper(): val for key, val in
            yaml.load(open(os.path.join(curdir, path))).items()
        }
        self.update(config_dict)

Flask.config_class = MyConfig
# github.com/rochacbruno/dynaconf

app = Flask(__name__)
app.config.from_yaml('settings.yaml')


@app.route("/")
def home():
    return "hello world"

@app.route("/hello/<name>")
def hello(name):
    return f"hello {name}"

app.run(use_reloader=True)
