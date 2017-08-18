from flask import Flask, request
from flask_classy import FlaskView, route

app = Flask(__name__)
app.config.from_object('settings')


class AwesomeView(FlaskView):
    def index(self):
        return "this is home"

    def get(self, id):
        return f'You want record with id {id}'

    def post(self):
        return f'You posted data: {dict(request.form)}'

    def qualquercoisa(self):
        return "Qualquer Coisa!"

    @route('/hello/')
    def custom(self):
        return "Custom route"

AwesomeView.register(app)


app.run(use_reloader=True)
