from flask_jwt_extended import jwt_required, current_user, create_access_token

from app import app, jwt
from flask import request, redirect, jsonify, make_response

from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/protected')
@jwt_required()
def protected():
    return 'protected'


@app.route("/who_am_i", methods=["GET"])
@jwt_required()
def whoami():
    # We can now access our sqlalchemy User object via `current_user`.
    return jsonify(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username,
    )


@app.route('/login')
def login():
    auth = request.authorization
    if auth:
        username = auth.username
        password = auth.password
        user = User.query.filter_by(username=username).one_or_none()
        if not user or not user.check_password(password):
            return jsonify("Wrong username or password"), 401
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})