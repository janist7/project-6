from flask import Flask, g, render_template, request, redirect, url_for
from app.database import db
from app.extensions import (
    lm, api, travis, mail, heroku, bcrypt, celery, babel, csrf
)
from app.assets import assets
import app.utils as utils
from app import config
from app.user import user
from app.categories import categories
from app.recipes import recipes
from app.auth import auth
import time
import sys
import os.path


def create_app(config=config.base_config):
    app = Flask(__name__)
    app.config.from_object(config)

    reload(sys)
    sys.setdefaultencoding('utf8')

    install_secret_key(app)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_jinja_env(app)

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(config.SUPPORTED_LOCALES)

    @app.before_request
    def before_request():
        g.request_start_time = time.time()
        g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)
        g.pjax = 'X-PJAX' in request.headers

    @app.route('/', methods=['GET'])
    def index():
        return redirect(url_for('categories.showCategories'))

    return app


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


def register_blueprints(app):
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(auth)
    app.register_blueprint(categories)
    app.register_blueprint(recipes)


def register_errorhandlers(app):
    def render_error(e):
        return render_template('errors/%s.html' % e.code, reason=e.description), e.code

    for e in [400, 401, 404, 500]:
        app.errorhandler(e)(render_error)


def register_jinja_env(app):
    app.jinja_env.globals['url_for_other_page'] = utils.url_for_other_page
    app.jinja_env.globals['timeago'] = utils.timeago

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
        print 'Error: No secret key. Create it with:'
        if not os.path.isdir(os.path.dirname(filename)):
            print 'mkdir -p', os.path.dirname(filename)
        print 'head -c 24 /dev/urandom >', filename
        sys.exit(1)
