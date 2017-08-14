from flask import Flask
from flask import request
from flask import jsonify
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

app.run(use_reloader=True)
