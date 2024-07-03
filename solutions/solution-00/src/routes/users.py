"""
This module contains the routes for the users endpoints.
"""

from flask import Blueprint
from src.models.user import User
from flask_bcrypt import Bcrypt
from flask import Flask, jsonify, request
from flask_jwt_extended import get_jwt_identity
from flask_bcrypt import Bcrypt
from flask_jwt_extended import jwt_required

from src.controllers.users import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)
bcrypt = Bcrypt()
users_bp = Blueprint("users", __name__, url_prefix="/users")

#users_bp.route("/", methods=["GET"])(get_users)
#users_bp.route("/", methods=["POST"])(create_user)
#users_bp.route("/<user_id>", methods=["GET"])(get_user_by_id)
#users_bp.route("/<user_id>", methods=["PUT"])(update_user)
#users_bp.route("/<user_id>", methods=["DELETE"])(delete_user)




@users_bp.route("/", methods=['GET', 'POST'])
@jwt_required()
def protected1():
    current_user = get_jwt_identity()
    if current_user:
        if request.method == 'GET':

            return get_users()
        elif request.method == 'POST':
            return create_user()
    else:
        return "Unauthorized", 401
    
    



@users_bp.route("/<user_id>", methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def protected2():
    current_user = get_jwt_identity()
    if current_user:
        if request.method == 'GET':
            return get_user_by_id()
        elif request.method == 'PUT':
            return update_user()
        elif request.method == 'DELETE':
            return delete_user()
    else:
        return "Unauthorized", 401