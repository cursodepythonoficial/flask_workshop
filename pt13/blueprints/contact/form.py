from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    message = TextAreaField('message', validators=[DataRequired()])
