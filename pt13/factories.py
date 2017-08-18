# The factory pattern

from flask import Flask, render_template, Markup, abort
from blueprints import home, mistake, secret
# from admin import configure_admin
# from flask_simplelogin import SimpleLogin
# from flask_debugtoolbar import DebugToolbarExtension


def create_app(**config):
    app = Flask(__name__)
    app.config.update(**config)
    return app


def configure_error_handlers(app):

    @app.errorhandler(404)
    @app.errorhandler(403)
    @app.errorhandler(500)
    def error_handler(error):
        return render_template('error.html', error=error), error.code


def configure_jinja(app):

    @app.template_global()
    @app.template_filter(name='listify')
    def ulfy(text):
        res = ['<ul>']
        lis = text.split()
        for li in lis:
            res.append(f'<li>{li}</li>')
        res.append('</ul>')
        return Markup('\n'.join(res))


def configure_blueprints(app):
    app.register_blueprint(home.blueprint)
    app.register_blueprint(mistake.blueprint)
    app.register_blueprint(secret.blueprint)


def configure_extensions(app):
    """Configure extensions"""
    # configure_admin(app)
    # TODO: pass custom `login_checker` which checks database
    # SimpleLogin(app)
    # DebugToolbarExtension(app)
