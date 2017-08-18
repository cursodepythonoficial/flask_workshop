# example from https://github.com/rochacbruno/flask_simple_sitemap

from functools import wraps
from flask import (
    Blueprint, render_template, abort, session,
    request, redirect, flash, url_for
)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('message', validators=[DataRequired()])


def default_login_checker(user):
    """user must be a dictionary here default is
    checking username/password
    if login is ok returns True else False
    In real implementation this function goes to database
    and checks login credentials.
    """
    username = user.get('username')
    password = user.get('password')
    if username == 'admin' and password == 'secret':
        return True
    return False


def is_logged_in():
    return 'logged_in' in session


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('simple_login.login'))
    return wrap


class SimpleLogin(object):
    """Simple Flask Login"""

    def __init__(self, app=None, login_checker=None):
        self.config = {
            'blueprint': 'simple_login',
            'login_url': '/login/',
            'logout_url': '/logout/',
            'home_url': '/'
        }
        self.app = None
        self.login_checker = None
        if app is not None:
            self.init_app(app=app, login_checker=login_checker)

    def init_app(self, app, login_checker=None):
        self.login_checker = login_checker or default_login_checker
        self._register(app)
        self._load_config()
        self._register_views()
        self._register_extras()

    def _register(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}

        if 'simple_login' in app.extensions:
            raise RuntimeError("Flask extension already initialized")

        app.extensions['simple_login'] = self
        self.app = app

    def _load_config(self):
        self.config.update(
            self.app.config.get_namespace(
                namespace='SIMPLE_LOGIN_',
                lowercase=True,
                trim_namespace=True
            )
        )

    def _register_views(self):
        self.blueprint = Blueprint(
            self.config['blueprint'],
            __name__,
            template_folder='templates'
        )

        self.blueprint.add_url_rule(
            self.config['login_url'],
            endpoint='login',
            view_func=self.login,
            methods=['GET', 'POST']
        )

        self.blueprint.add_url_rule(
            self.config['logout_url'],
            endpoint='logout',
            view_func=self.logout,
            methods=['GET']
        )

        self.app.register_blueprint(self.blueprint)

    def _register_extras(self):
        self.app.add_template_global(is_logged_in)

    def login(self):
        destiny = request.args.get(
            'next', default=self.config.get('home_url', '/')
        )
        if is_logged_in():
            flash('already logged in')
            return redirect(destiny)

        form = LoginForm()
        if form.validate_on_submit():
            if self.login_checker(form.data):
                flash("login success!!")
                session['logged_in'] = True
                return redirect(destiny)
            else:
                flash('invalid credentials')
        return render_template('login.html', form=form)

    def logout(self):
        session.clear()
        flash('Logged out!')
        return redirect(self.config.get('home_url', '/'))
