# github.com/flask-admin/flask-admin/blob/master/examples/tinymongo/app.py

from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView
from wtforms import fields, form
from db import db


# forms

class MenuForm(form.Form):
    name = fields.StringField('name')
    endpoint = fields.StringField('endpoint')


class ContactForm(form.Form):
    name = fields.StringField('name')
    message = fields.TextAreaField('message')


# admin views

class MenuView(ModelView):
    column_list = ('name', 'endpoint')
    column_sortable_list = ('name', 'endpoint')
    form = MenuForm


class ContactView(ModelView):
    column_list = ('name',)
    column_sortable_list = ('name',)
    form = ContactForm

    def is_accessible(self):
        # TODO: protect with simple_login
        return True


# admin factory
def configure_admin(app):
    admin = Admin(app, name='Flask Workshop')

    # add views
    admin.add_view(MenuView(db.menu, 'Menu'))
    admin.add_view(ContactView(db.contact, 'Contact'))
