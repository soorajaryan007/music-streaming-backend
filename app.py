from flask import Flask, jsonify, send_file, request,redirect,abort

from config import Config
from models import db,Song
from services.song_service import get_all_songs, get_all_users, get_song_by_title, get_song_id
from routes.song_routes import upload_song
from redis_client.cache import redis_client

app = Flask(__name__)
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
def play_song(song_id):

    cache_key = f"song:{song_id}"
    cached_song_url = None

    # 1️⃣ Try Redis
    try:
        cached_song_url = redis_client.get(cache_key)
    except Exception:
        print("Redis unavailable, skipping cache")

    if cached_song_url:
        print("Cache HIT")

        if Config.ENV == "production":
            return redirect(cached_song_url)
        else:
            return send_file(cached_song_url, mimetype="audio/mpeg")

    # 2️⃣ DB fallback
    print("Cache MISS")

    song = get_song_id(song_id)

    if not song:
        abort(404, description="Song not found")

    # 3️⃣ Try storing in Redis (non-critical)
    try:
        redis_client.set(cache_key, song.mp3_path, ex=3600)
    except Exception:
        print("Redis unavailable, cannot cache")

    # 4️⃣ Return response
    if Config.ENV == "production":
        return redirect(song.mp3_path)
    else:
        return send_file(song.mp3_path, mimetype="audio/mpeg")


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