# -*- coding: UTF-8 -*-

from settings import db
from settings import FEEDLY_REDIRECT_URI
from flask import Blueprint
from flask import request, redirect, g, render_template

from . import feedly_client


authentication = Blueprint('auth', __name__,
                 template_folder='templates')


@authentication.route('/auth')
def auth():
    # Redirect the user to the feedly authorization URL to get user code
    code_url = feedly_client.get_code_url(FEEDLY_REDIRECT_URI)
    return redirect(code_url)


#NOTE: callback must be on root URL as in route below (https://developer.feedly.com/v3/sandbox/)
@authentication.route('/')
def callback():
    code = request.args.get('code', '')
    if not code:
        return 'Authentication failed: param [code] was not returned from API.'

    # response of access token
    res_access_token = feedly_client.get_access_token(FEEDLY_REDIRECT_URI, code)

    # user id
    #TODO: render in a clean error template
    if 'errorCode' in res_access_token.keys():
        return 'Authentication failed: %s(%s)' % (res_access_token['errorCode'], res_access_token['errorMessage'])

    # store token in database
    tokens = db.tokens
    tokens.update(res_access_token, res_access_token, upsert=True)

    # write to file
    #id = res_access_token['id']
    #access_token = res_access_token['access_token']
    #with open(settings.ACCESS_TOKEN_FILE, 'w') as f:
    #    f.write(access_token)

    return render_template("success.html")


def after_this_request(f):
    if not hasattr(g, 'after_request_callbacks'):
        g.after_request_callbacks = []
    g.after_request_callbacks.append(f)
    return f


@authentication.after_request
def call_after_request_callbacks(response):
    for callback in getattr(g, 'after_request_callbacks', ()):
        response = callback(response)
    return response

