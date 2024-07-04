"""
This module contains the routes for the reviews blueprint
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask import Flask, jsonify, request
from flask_jwt_extended import get_jwt_identity
from flask import Flask, jsonify, request
from src.controllers.reviews import (
    create_review,
    delete_review,
    get_reviews_from_place,
    get_reviews_from_user,
    get_review_by_id,
    get_reviews,
    update_review,
)

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route("/places/<place_id>/reviews", methods=['POST'])
@jwt_required()
def post_review(place_id):
    current_user = get_jwt_identity()
    if current_user:
        return create_review(place_id)
    else:
        return "Unauthorized", 401
    


@reviews_bp.route("/places/<place_id>/reviews")
@jwt_required()
def retrieves_review_from_place(place_id):
    current_user = get_jwt_identity()
    if current_user:
        return get_reviews_from_place(place_id)
    else:
        return "Unauthorized", 401
    


@reviews_bp.route("/users/<user_id>/reviews")
@jwt_required()
def retrieves_user_review(user_id):
    current_user = get_jwt_identity()
    if current_user:
        return get_reviews_from_user(user_id)
    else:
        return "Unauthorized", 401
    



@reviews_bp.route("/reviews", methods=["GET"])
@jwt_required()
def retrieves_reviews():
    current_user = get_jwt_identity()
    if current_user:
        return get_reviews()

    else:
        return "Unauthorized", 401
    
@reviews_bp.route("/reviews/<review_id>", methods=["GET"])
@jwt_required()
def retrieves_review_by_id(review_id):
    current_user = get_jwt_identity()
    if current_user:
        return get_review_by_id(review_id)

    else:
        return "Unauthorized", 401
    


@reviews_bp.route("/reviews/<review_id>", methods=["PUT"])
@jwt_required()
def modify_review(review_id):
    current_user = get_jwt_identity()
    if current_user:
        return update_review(review_id)

    else:
        return "Unauthorized", 401
    
    


@reviews_bp.route("/reviews/<review_id>", methods=["DELETE"])
@jwt_required()
def remove_review(review_id):
    current_user = get_jwt_identity()
    if current_user:
         return delete_review(review_id)

    else:
        return "Unauthorized", 401
   
