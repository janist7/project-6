import os.path
import sys
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, g, render_template, request, redirect, url_for
from database import db
from extensions import (
    lm, api, travis, mail, heroku, bcrypt, celery, babel, csrf
)
from assets import assets
import utils as utils
import config
from user import user
from categories import categories
from recipes import recipes
from auth import auth
from categories.models import Category
from recipes.models import Recipe
import time
import json
import importlib

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
    app.jinja_env.globals['url_for_other_page'] = utils.url_for_other_page
    app.jinja_env.globals['timeago'] = utils.timeago


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
        GOOGLE_CLIENT_ID = json.loads(open(filename, 'r').read())['web']['client_id']
    except:
        print('Did not find a client_secrets.json at:')
        print(os.path.dirname(filename))
        os._exit(1)

application = Flask(__name__)
application.config.from_object(config.base_config)

# Runs all initialization functions
install_secret_key(application)
install_client_secret(application)
register_extensions(application)
register_blueprints(application)
register_errorhandlers(application)
register_jinja_env(application)

    # Enables api endpoints example user for all info is:
    # /api/category?q={%22filters%22:[{%22name%22:%22name%22,%22op%22:%22ge%22,%22val%22:%22%22}]}
    #
    # Getting just one category is:
    # /api/category/19, same for recipe (api/{Category, Recipe}}/id) etc.
    #
    # Example for all Recipes in category 22:
    # /api/recipe?q={%22filters%22:[{%22name%22:%22category_id%22,%22op%22:%22==%22,%22val%22:%2219%22}]}
    #
    # How to use - https://flask-restless.readthedocs.io/en/0.12.0/searchformat.html#searchformat
enable_api_endpoints(True)

    # @babel.localeselector
    # def get_locale():
    #   return request.accept_languages.best_match(config.SUPPORTED_LOCALES)


@application.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)
    g.pjax = 'X-PJAX' in request.headers


@application.route('/', methods=['GET'])
def index():
    return redirect(url_for('categories.showCategories'))


if __name__ == '__main__':
    install_secret_key(application)
    install_client_secret(application)
    application.run("0.0.0.0")
