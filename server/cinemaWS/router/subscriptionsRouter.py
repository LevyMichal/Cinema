# subscriptions_routes.py
from flask import Blueprint, jsonify, request
from BLL.subscriptions_WS_BLL import SubscriptionsBLL

# Creating a Flask Blueprint named 'subscriptions'
subscriptions = Blueprint("subscriptions", __name__)
subscriptions_bll = SubscriptionsBLL()


# Movies Endpoints
@subscriptions.route("/movies", methods=["GET"])
def get_all_movies():
    """Get all movies"""
    return jsonify(subscriptions_bll.get_all_movies())


@subscriptions.route("/movies/<movie_id>", methods=["GET"])
def get_movie_by_id(movie_id):
    """Get a specific movie by ID"""
    return jsonify(subscriptions_bll.get_movie_by_id(movie_id))


@subscriptions.route("/movies", methods=["POST"])
def create_movie():
    """Create a new movie"""
    data = request.get_json()
    return jsonify(subscriptions_bll.create_movie(data)), 201


@subscriptions.route("/movies/<movie_id>", methods=["PUT"])
def update_movie(movie_id):
    """Update a specific movie by ID"""
    data = request.get_json()
    return jsonify(subscriptions_bll.update_movie(movie_id, data))


@subscriptions.route("/movies/<movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    """Delete a specific movie by ID"""
    return jsonify(subscriptions_bll.delete_movie(movie_id))


# Members Endpoints
@subscriptions.route("/members", methods=["GET"])
def get_all_members():
    """Get all members"""
    return jsonify(subscriptions_bll.get_all_members())


@subscriptions.route("/members/<member_id>", methods=["GET"])
def get_member_by_id(member_id):
    """Get a specific member by ID"""
    return jsonify(subscriptions_bll.get_member_by_id(member_id))


@subscriptions.route("/members", methods=["POST"])
def create_member():
    """Create a new member"""
    data = request.get_json()
    return jsonify(subscriptions_bll.create_member(data)), 201


@subscriptions.route("/members/<member_id>", methods=["PUT"])
def update_member(member_id):
    """Update a specific member by ID"""
    data = request.get_json()
    return jsonify(subscriptions_bll.update_member(member_id, data))


@subscriptions.route("/members/<member_id>", methods=["DELETE"])
def delete_member(member_id):
    """Delete a specific member by ID"""
    return jsonify(subscriptions_bll.delete_member(member_id))


# Subscriptions Endpoints
@subscriptions.route("/subscriptions", methods=["GET"])
def get_all_subscriptions():
    """Get all subscriptions"""
    return jsonify(subscriptions_bll.get_all_subscriptions())


@subscriptions.route("/subscriptions/<subscription_id>", methods=["GET"])
def get_subscription_by_id(subscription_id):
    """Get a specific subscription by ID"""
    return jsonify(subscriptions_bll.get_subscription_by_id(subscription_id))


@subscriptions.route("/subscriptions", methods=["POST"])
def create_subscription():
    """Create a new subscription"""
    data = request.get_json()
    return jsonify(subscriptions_bll.create_subscription(data))


@subscriptions.route("/subscriptions/<subscription_id>", methods=["PUT"])
def update_subscription(subscription_id):
    """Update a specific subscription by ID"""
    data = request.get_json()
    return jsonify(subscriptions_bll.update_subscription(subscription_id, data))


@subscriptions.route("/subscriptions/<subscription_id>", methods=["DELETE"])
def delete_subscription(subscription_id):
    """Delete a specific subscription by ID"""
    return jsonify(subscriptions_bll.delete_subscription(subscription_id))
