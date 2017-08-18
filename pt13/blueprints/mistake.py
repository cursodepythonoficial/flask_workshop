from flask import Blueprint, abort

blueprint = Blueprint('mistake', __name__)


@blueprint.route('/mistake/')
def mistake():
    # this causes Internal Server Error
    return abort(500)
