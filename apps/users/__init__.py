from flask import Blueprint
from flask_login import LoginManager

login_manager = LoginManager()
user_blueprint = Blueprint('user_bp', __name__, template_folder='templates')

from . import view