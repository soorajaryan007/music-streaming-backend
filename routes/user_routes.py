from flask import Blueprint, jsonify
from services.song_service import get_all_users

user_bp = Blueprint("users", __name__)

@user_bp.route("/users")
def get_users():
    users = get_all_users()
    return jsonify(users)