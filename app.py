from flask import Flask, jsonify, send_file, request,redirect,abort
from config import Config
from models import db,Song
from services.song_service import get_all_songs, get_all_users, get_song_by_title, get_song_id
from routes.song_routes import upload_song

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
    song = get_song_id(song_id)

    if not song:
        abort(404, description="Song not found")

    try:
        if Config.ENV == "production":
            return redirect(song.mp3_path)  # S3 URL
        else:
            return send_file(song.mp3_path, mimetype="audio/mpeg")
    except Exception as e:
        abort(500, description=str(e))


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