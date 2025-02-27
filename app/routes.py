from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.services import get_users, get_user, create_user, update_user, delete_user

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users", methods=["GET"])
def get_all_users():
    users = get_users()
    return jsonify(users), 200

@user_routes.route("/users/<id>", methods=["GET"])
def get_single_user(id):
    user = get_user(ObjectId(id))
    return jsonify(user) if user else ("User not found", 404)

@user_routes.route("/users", methods=["POST"])
def add_user():
    data = request.json
    if not data or not all(k in data for k in ("name", "email", "password")):
        return jsonify({"error": "Missing fields"}), 400

    create_user(data)
    return jsonify({"message": "User created"}), 201

@user_routes.route("/users/<id>", methods=["PUT"])
def modify_user(id):
    data = request.json
    update_user(ObjectId(id), data)
    return jsonify({"message": "User updated"}), 200

@user_routes.route("/users/<id>", methods=["DELETE"])
def remove_user(id):
    delete_user(ObjectId(id))
    return jsonify({"message": "User deleted"}), 200
