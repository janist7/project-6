""" Google OAuth view """

from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
    make_response
)
from flask import session as login_session
from flask_babel import gettext
from flask_login import login_user, login_required, logout_user
from itsdangerous import URLSafeSerializer, BadSignature
from user.models import User
from user.forms import RegisterUserForm
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from .forms import LoginForm
from auth import auth
import httplib2
import json
import requests
import sys
import os.path

APPLICATION_NAME = "Recipes Website"

@auth.route('/gconnect', endpoint='gconnect', methods=['POST'])
def gconnect():
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != GOOGLE_CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    user = User.query.filter_by(email=data['email']).first()
    # see if user exists, if it doesn't make a new one
    if not user:
        user = User.create(
            username=data['name'],
            email=data['email'],
            remote_addr=request.remote_addr
        )
    else:
        login_user(user)
    # Returns name for flash message
    return data['name']
