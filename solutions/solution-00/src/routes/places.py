"""
This module contains the routes for the places blueprint
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from src.controllers.places import (
    create_place,
    delete_place,
    get_place_by_id,
    get_places,
    update_place,
)

places_bp = Blueprint("places", __name__, url_prefix="/places")

#places_bp.route("/", methods=["GET"])(get_places)
#places_bp.route("/", methods=["POST"])(create_place)

#places_bp.route("/<place_id>", methods=["GET"])(get_place_by_id)
#places_bp.route("/<place_id>", methods=["PUT"])(update_place)
#places_bp.route("/<place_id>", methods=["DELETE"])(delete_place)

@places_bp.route('/', methods=["GET"])
@jwt_required()
def get_all_places():
    get_places()

@places_bp.route('/', methods=['POST'])
@jwt_required()
def post_a_place():
    create_place()

@places_bp.route('/<place_id>', methods=["GET"])
@jwt_required()
def retrieves_place():
    get_place_by_id()

@places_bp.route('/<place_id>', methods=['PUT'])
@jwt_required()
def update_a_place():
    update_place()

@places_bp.route('/<place_id>', methods=['DELETE'])
@jwt_required()
def protected():
    delete_place()
