"""
This module contains the routes for the cities blueprint
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask import Flask, jsonify, request
from flask_jwt_extended import get_jwt_identity
from src.controllers.cities import (
    create_city,
    delete_city,
    get_city_by_id,
    get_cities,
    update_city,
)

cities_bp = Blueprint("cities", __name__, url_prefix="/cities")

#cities_bp.route("/", methods=["GET"])(get_cities)
#cities_bp.route("/", methods=["POST"])(create_city)

#cities_bp.route("/<city_id>", methods=["GET"])(get_city_by_id)
#cities_bp.route("/<city_id>", methods=["PUT"])(update_city)
#cities_bp.route("/<city_id>", methods=["DELETE"])(delete_city)


@cities_bp.route('/', methods=['GET'])
@jwt_required()
def all_cities():
    current_user = get_jwt_identity()
    if current_user:
        return get_cities()
    else:
        return "Unauthorized", 401
    

@cities_bp.route('/', methods=['POST'])
@jwt_required()
def post_city():
    current_user = get_jwt_identity()
    if current_user:
        return create_city()
    else:
        return "Unauthorized", 401
    

@cities_bp.route('/<city_id>', methods=['GET'])
@jwt_required()
def retrieves_citys(city_id):
    current_user = get_jwt_identity()
    if current_user:
        return get_city_by_id(city_id)
    else:
        return "Unauthorized", 401
    

@cities_bp.route('/<city_id>', methods=['PUT'])
@jwt_required()
def modify_city(city_id):
    current_user = get_jwt_identity()
    if current_user:
        return update_city(city_id)
    else:
        return "Unauthorized", 401
    

@cities_bp.route('/<city_id>', methods=['DELETE'])
@jwt_required()
def remove_city(city_id):
    current_user = get_jwt_identity()
    if current_user:
        return delete_city(city_id)
    else:
        return "Unauthorized", 401
    
