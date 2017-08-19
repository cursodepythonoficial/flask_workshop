import logging
from flask import Flask, render_template, flash, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret-here'
DebugToolbarExtension(app)


@app.route("/")
def home():
    logger.error('Hello on logger ')
    flash('Hello')
    return render_template('index.html')


@app.route("/debug")
def debug():
    name = request.args.get('name', 'world')
    import ipdb; ipdb.set_trace()
    msg = "Hello"
    return f'{msg}, {name}'


@app.route('/api/<operation>/', methods=['POST'])
def api(operation):
    """
    curl -XPOST http://localhost:5000/api/sum/ -d "x=1&y=20"
    http -f post http://localhost:5000/api/sum/ x=1 y=20
    """

    x = int(request.form.get('x'))
    y = int(request.form.get('y'))

    operations = {
        'sum': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y,
        'div': lambda x, y: x / y,
    }
    result = operations[operation](x, y)
    return jsonify(x=x, y=y, operation=operation, result=result)


if __name__ == "__main__":
    app.run(use_reloader=True)
