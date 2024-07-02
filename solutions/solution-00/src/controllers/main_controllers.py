from flask import abort, request, jsonify
from src.models.user import User
from flask_jwt_extended import create_access_token, get_jwt_identity
import bcrypt

def login_user():
    data = request.get_json()
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
         access_token = create_access_token(identity=email)
         return jsonify(access_token=access_token), 200
    return 'Wrong username or password', 401