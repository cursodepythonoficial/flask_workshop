from flask import Blueprint, render_template
from .form import ContactForm
from .db import db

blueprint = Blueprint('contact', __name__, template_folder='templates')


@blueprint.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        db.contact.insert(form.data)
        return "Mensagem enviada com sucesso!"
    return render_template('contact.html', form=form)
