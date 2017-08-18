# The factory pattern

from flask import Flask, render_template, Markup, abort


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


def configure_views(app):

    @app.route('/')
    def home():
        return render_template('ok.html')

    @app.route('/mistake')
    def mistake():
        # this causes Internal Server Error
        return abort(500)


    @app.route('/secret')
    def secret():
        # this causes Foridden (user not authorized)
        return abort(403)
