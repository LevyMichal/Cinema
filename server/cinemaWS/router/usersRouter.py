from flask import Blueprint, jsonify, request
from BLL.usersBLL import UsersBLL

users = Blueprint("users", __name__)
users_BLL = UsersBLL()


# GET ALL users
@users.route("/", methods=["GET"])
def get_all():
    all_users = users_BLL.get_all_users()
    return jsonify(all_users)


@users.route("/<id>", methods=["GET"])
def get_one(id):
    user = users_BLL.get_user_by_id(id)
    return jsonify(user)


@users.route("/username/<username>", methods=["GET"])
def get_one_by_username(username):
    user = users_BLL.get_user_by_username(username)
    return jsonify(user)


@users.route("/", methods=["POST"])
def create_user():
    new_user = request.json
    result = users_BLL.add_user(new_user)
    return jsonify(result)


@users.route("/<id>", methods=["PUT"])
def update_user(id):
    data = request.json
    fields_names = list(data.keys())
    updated_values = list(data.values())
    result = users_BLL.update_user(id, fields_names, updated_values)

    return jsonify(result)


@users.route("/<id>", methods=["DELETE"])
def delete_user(id):
    result = users_BLL.delete_user(id)
    return jsonify(result)
