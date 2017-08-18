from flask import Flask, render_template
from form import ContactForm

# from utils import build_menu_item, build_menu_item_as_filter

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = "secret-here"

# app.add_template_global(build_menu_item)
# app.add_template_filter(build_menu_item_as_filter, name='menu')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return "Mensagem enviada com sucesso!"
    return render_template('contact.html', form=form)
