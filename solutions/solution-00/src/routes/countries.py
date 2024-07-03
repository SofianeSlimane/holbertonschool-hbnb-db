"""
This module contains the routes for the countries endpoint
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask import Flask, jsonify, request
from flask_jwt_extended import get_jwt_identity
from src.controllers.countries import (
    get_countries,
    get_country_by_code,
    get_country_cities,
)

countries_bp = Blueprint("countries", __name__, url_prefix="/countries")

#countries_bp.route("/", methods=["GET"])(get_countries)
#countries_bp.route("/<code>", methods=["GET"])(get_country_by_code)
#countries_bp.route("/<code>/cities", methods=["GET"])(get_country_cities)


@countries_bp.route('/', methods=['GET'])
@jwt_required()
def all_countries():
    current_user = get_jwt_identity()
    if current_user:
        return get_countries
    else:
        return "Unauthorized", 401
    

@countries_bp.route('/<code>', methods=['GET'])
@jwt_required()
def post_country():
    current_user = get_jwt_identity()
    if current_user:
        return get_country_by_code
    else:
        return "Unauthorized", 401
    
@countries_bp.route('/<code>/cities', methods=['GET'])
@jwt_required()
def retrieves_country_cities():
    current_user = get_jwt_identity()
    if current_user:
        return get_country_cities
    else:
        return "Unauthorized", 401
    
