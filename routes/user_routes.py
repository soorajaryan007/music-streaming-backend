from flask import Blueprint, jsonify
from services.song_service import SongService

user_bp = Blueprint("users", __name__)

s = SongService()
get_all_users =s.get_all_users

@user_bp.route("/users")
def get_users():
    users = get_all_users()
    return jsonify(users)