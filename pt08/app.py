from uuid import uuid4

from flask import (
    Flask,
    abort,
    flash,
    jsonify,
    render_template,
    request,
    session
)

from form import MyForm
from functions import upperfy

app = Flask(__name__)
app.config.from_json('settings.json')

@app.route("/")
def home():
    return "hello world"


@app.route("/hello/<name>")
def hello(name):
    return f"hello {name}"


app.add_url_rule(
    rule="/upperfy/<text>",
    view_func=upperfy
)

# curl -XPOST http://localhost:5000/getecho  (Not Allowed)
# Browse: http://localhost:5000/getecho?a=b&c=d&e=f&e=g

@app.route('/getecho')  # methods=[HEAD,OPTIONS,GET]
def getecho():
    return jsonify(data=dict(request.args))

# curl -XPOST http://localhost:5000/formecho -d '{"a": "b"}'
# http --form localhost:5000/formecho a=b

@app.route('/formecho', methods=['POST'])
def formecho():
    return jsonify(data=request.form)

# curl -XPOST -H "Content-Type:application/json" http://localhost:5000/jsonecho -d '{"a": "b"}'
# http post localhost:5000/jsonecho a=b
@app.route('/jsonecho', methods=['POST'])
def jsonecho():
    return jsonify(data=request.json)

# echo "Hello Flask" > /tmp/flask.txt
# http --form post localhost:5000/fileecho name='flask' myfile@/tmp/flask.txt

@app.route('/fileecho', methods=['POST'])
def fileecho():
    myfile = request.files['myfile']
    # myfile.save('path/to/save')
    return jsonify(
        data=request.form,
        filename=myfile.filename,
        stream=str(myfile.stream.read())
    )


# FORMS

@app.route('/htmlform', methods=['GET', 'POST'])
def htmlform():
    if request.method == 'GET':
        # return the html form to be filled
        return render_template('htmlform.html')

    # if it is a POST capture the data
    name = request.form.get('name')
    level = request.form.get('level')
    content = request.files.get('content')

    # How to validate?

    # process data and return the result
    return render_template(
        'success.html', name=name, level=level, content=content.stream.read()
    )

# CSRF SAFE FORM

@app.route('/safeform', methods=['GET', 'POST'])
def safeform():
    if request.method == 'GET':
        # 1) generate a token and save in the session
        # 2) include the token in the FORM
        # return the html form to be filled
        safetoken = session['token'] = session.get('token', uuid4())
        return render_template('safeform.html', token=safetoken)

    # if it is a POST capture the data
    name = request.form.get('name')
    level = request.form.get('level')
    content = request.files.get('content')
    formtoken = request.form.get('token')

    # check the token
    safetoken = session.get('token')
    if not safetoken or str(safetoken) != str(formtoken):
        abort(500, f"Invalid!! {safetoken} != {formtoken}")

    # process data and clean token and return the result
    del session['token']
    return render_template(
        'success.html', name=name, level=level, content=content.stream.read()
    )



# WTFORM

@app.route('/wtform', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return render_template(
            'success.html',
            name=form.name.data,
            level=form.level.data,
            content=form.content.data.stream.read()
        )
    return render_template('wtform.html', form=form)
