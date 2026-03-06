import time

from flask_cors import CORS
from flask import Flask, jsonify, send_file, request,redirect,abort
from services.song_service import get_song_url
from utils.response_handler import stream_song
from config import Config
from models import db,Song
from services.song_service import get_all_songs, get_all_users, get_song_by_title, get_song_id
from routes.song_routes import upload_song
from api_latency.latency import measure_latency

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db.init_app(app)


# -----------------------------
# Health Check
# -----------------------------
@app.route("/")
def home():
    return {"message": "Spotify Clone Running 🎵"}


# -----------------------------
# Get all songs
# -----------------------------
@app.route("/songs")
def get_songs():
    songs = get_all_songs()

    return jsonify(songs)


# -----------------------------
# Stream song
# -----------------------------

@app.route("/play/<int:song_id>")
@measure_latency
def play_song(song_id):
    song_url = get_song_url(song_id)
    if not song_url:
        abort(404)
    return stream_song(song_url)

# -----------------------------
# Get users
# -----------------------------
@app.route("/users")
def get_users():
    users = get_all_users()
    return jsonify(users)

# ---------------------------------
# Search song by name
# ---------------------------------
@app.route("/songs/search")
def search_song():
    song_name = request.args.get("title")

    if not song_name:
        return jsonify({"error": "title query parameter required"}), 400

    songs = get_song_by_title(song_name)

    if not songs:
        return jsonify({"message": "No songs found"}), 404

    return jsonify(songs)



@app.route("/upload-song", methods=["POST"])
def upload_song_route():
    return upload_song()

if __name__ == "__main__":
    app.run(debug=True)