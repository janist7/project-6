""" All Auhentification related views """

from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from flask_babel import gettext
from flask_login import login_user, login_required, logout_user
from flask import session as login_session
from itsdangerous import URLSafeSerializer, BadSignature
from app.extensions import lm
from app.tasks import send_registration_email
from app.user.models import User
from app.user.forms import RegisterUserForm
from .forms import LoginForm
from ..auth import auth, controller
from app.utils import babel_flash_message
import httplib2

# Probably should be server side as cookies are not that safe
# (https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session)


@lm.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        babel_flash_message('You were logged in as {data}', form.user.username)
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('forms/login.html', form=form)


@auth.route('/oauth', methods=['POST'])
def oauth():
    name = request.data
    babel_flash_message('You were connected as {data}', name)
    return redirect(request.args.get('next') or url_for('index'))


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    # Disconnect a regular user.
    access_token = login_session.get('access_token')
    if access_token is None:
        logout_user()
        login_session.clear()
        babel_flash_message('You were logged out')
        return redirect(url_for('.login'))
    # Disconnect a google account user.
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['provider']
        logout_user()
        login_session.clear()
        babel_flash_message('Successfully disconnected')
        return redirect(url_for('.login'))
    else:
        babel_flash_message('Failed to revoke token for given user')
        logout_user()
        login_session.clear()
        return redirect(url_for('.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterUserForm()
    if form.validate_on_submit():
        user = controller.createNewUser(form.data['username'],             form.data['email'], form.data['password'], request.remote_addr)
        s = URLSafeSerializer(current_app.secret_key)
        token = s.dumps(user.id)
        send_registration_email.delay(user, token)
        babel_flash_message('Sent verification email to {data}', user.email)
        return redirect(url_for('index'))
    return render_template('forms/register.html', form=form)


@auth.route('/verify/<token>', methods=['GET'])
def verify(token):
    s = URLSafeSerializer(current_app.secret_key)
    try:
        id = s.loads(token)
    except BadSignature:
        abort(404)

    user = controller.getUser(id)
    if user.active:
        abort(404)
    else:
        user.active = True
        user.update()
        babel_flash_message('Registered user {data}. Please login to continue.', user.username)
        return redirect(url_for('auth.login'))
