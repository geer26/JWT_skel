from flask_jwt_extended import jwt_required

from app import app, jwt
from flask import request, redirect, Response

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/protected')
@jwt_required()
def protected():
    return 'protected'


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        return redirect('/protected')
    #return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    resp = Response()
    resp.data = '<h1>LOGINPAGE</h1>'
    resp.headers['WWW-Authenticate'] = 'Basic'
    return resp, 401