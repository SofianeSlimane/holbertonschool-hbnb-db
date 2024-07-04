
from flask import Blueprint
from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token
from src.controllers.main_controllers import login_user

main_bp = Blueprint("main", __name__)
@main_bp.route('/login', methods=['POST'])
def login():
    return login_user()