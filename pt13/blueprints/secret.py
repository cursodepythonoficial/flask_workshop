# TODO: protect with simplelogin
from flask import Blueprint, abort

blueprint = Blueprint('secret', __name__)


@blueprint.route('/secret/')
def secret():
    # this causes Foridden (user not authorized)
    return abort(403)
