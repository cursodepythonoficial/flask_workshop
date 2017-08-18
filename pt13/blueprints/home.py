from flask import Blueprint, render_template

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def home():
    return render_template('ok.html')


@blueprint.app_template_global()
def foo():
    return 'bar'
