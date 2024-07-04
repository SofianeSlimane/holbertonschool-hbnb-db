"""
This module contains the routes for the amenities blueprint
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask import Flask, jsonify, request
from flask_jwt_extended import get_jwt_identity
from src.controllers.amenities import (
    create_amenity,
    delete_amenity,
    get_amenity_by_id,
    get_amenities,
    update_amenity,
)

amenities_bp = Blueprint("amenities", __name__, url_prefix="/amenities")

#amenities_bp.route("/", methods=["GET"])(get_amenities)
#amenities_bp.route("/", methods=["POST"])(create_amenity)

#amenities_bp.route("/<amenity_id>", methods=["GET"])(get_amenity_by_id)
#amenities_bp.route("/<amenity_id>", methods=["PUT"])(update_amenity)
#amenities_bp.route("/<amenity_id>", methods=["DELETE"])(delete_amenity)

@amenities_bp.route("/", methods=['GET'])
@jwt_required()
def all_amenities():
    current_user = get_jwt_identity()
    if current_user:
        return get_amenities()
    else:
        return "Unauthorized", 401
    
@amenities_bp.route("/", methods=['POST'])
def post_amenity():
    return create_amenity()
    
@amenities_bp.route("/<amenity_id>", methods=['GET'])
@jwt_required()
def retrieves_amenity(amenity_id):
    current_user = get_jwt_identity()
    if current_user:
       return get_amenity_by_id(amenity_id)
    else:
        return "Unauthorized", 401
    
@amenities_bp.route("/<amenity_id>", methods=['PUT'])
@jwt_required()
def modify_amenity(amenity_id):
    current_user = get_jwt_identity()
    if current_user:
       return update_amenity(amenity_id)
    else:
        return "Unauthorized", 401
    
@amenities_bp.route("/<amenity_id>", methods=['DELETE'])
@jwt_required()
def remove_amenity(amenity_id):
    current_user = get_jwt_identity()
    if current_user:
       return delete_amenity(amenity_id)
    else:
        return "Unauthorized", 401
    