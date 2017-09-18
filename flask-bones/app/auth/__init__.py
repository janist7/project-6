from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates')

import views
# imports also google oauth
import google_oauth
