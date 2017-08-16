from flask import Flask
from views import MyView

app = Flask(__name__)
app.config.from_object('settings')

app.add_url_rule(
    '/',
    view_func=MyView.as_view('myview')
)
