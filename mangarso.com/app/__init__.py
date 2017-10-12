import time
import json
import importlib
import sys
import os.path
from flask import Flask, g, render_template, request, redirect, url_for

app = Flask(__name__)

from app.config import dev_config, prod_config

app.config.from_object(dev_config)

from app.database import db
from app.extensions import (
    lm, api, travis, mail, heroku, bcrypt, celery, babel, csrf
)
from app.assets import assets
from app.utils import (
    flash_errors, babel_flash_message, url_for_other_page, timeago
)
from app.user import user
from app.categories import categories
from app.recipes import recipes
from app.auth import auth
from app.categories.models import Category
from app.recipes.models import Recipe



# Enables api endpoints, only Get for now
def enable_api_endpoints(enabled=False):
    if enabled is True:
        api.create_api(Category, methods=['GET'])
        api.create_api(Recipe, methods=['GET'])

# Lazy registering off extensions
def register_extensions(app):
    heroku.init_app(app)
    travis.init_app(app)
    db.init_app(app)
    api.init_app(app)
    lm.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    celery.config_from_object(app.config)
    assets.init_app(app)
    babel.init_app(app)
    csrf.init_app(app)


# Register all blueprints
def register_blueprints(app):
    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(categories)
    app.register_blueprint(recipes)


# Depending on which abort is trown, loads needed html
def register_errorhandlers(app):
    def render_error(e):
        return render_template('errors/%s.html' % e.code, reason=e.description), e.code

    for e in [400, 401, 404, 500]:
        app.errorhandler(e)(render_error)


# Register jinja for templating
def register_jinja_env(app):
    app.jinja_env.globals['url_for_other_page'] = url_for_other_page
    app.jinja_env.globals['timeago'] = timeago


# Auto install app secret key, if none found then prints how to make one
def install_secret_key(app, filename='secret_key'):
    """Configure the SECRET_KEY from a file
    in the instance directory.

    If the file does not exist, print instructions
    to create it from a shell with a random key,
    then exit.

    """
    filename = os.path.join(app.instance_path, filename)
    try:
        app.config['SECRET_KEY'] = open(filename, 'rb').read()
        app.config['WTF_CSRF_SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        print('Error: No secret key. Create it with:')
        if not os.path.isdir(os.path.dirname(filename)):
            print('mkdir -p', os.path.dirname(filename))
        print('head -c 24 /dev/urandom >', filename)
        os._exit(1)


def install_client_secret(app, filename='client_secrets.json'):
    try:
        filename = os.path.join(app.instance_path, filename)
        app.config['GOOGLE_CLIENT_ID'] = json.loads(open(filename, 'r').read())['web']['client_id']
    except Exception as e:
        print(e)
        print(os.path.dirname(filename))
        os._exit(1)

# Init stuff for app
install_secret_key(app)
install_client_secret(app)
register_extensions(app)
register_blueprints(app)
register_errorhandlers(app)
register_jinja_env(app)
enable_api_endpoints(True)


# @babel.localeselector
# def get_locale():
#   return request.accept_languages.best_match(config.SUPPORTED_LOCALES)


@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)
    g.pjax = 'X-PJAX' in request.headers


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('categories.showCategories'))
