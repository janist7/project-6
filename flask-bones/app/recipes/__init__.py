from flask import Blueprint

recipes = Blueprint('recipes', __name__, template_folder='templates')

import views
