from flask import Flask, jsonify, send_file, request
from config import Config
from models import db, User, Song

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
    songs = Song.query.all()

    return jsonify([
        {
            "id": s.id,
            "title": s.title,
            "artist": s.artist,
            "genre": s.genre,
        }
        for s in songs
    ])


# -----------------------------
# Stream song
# -----------------------------
@app.route("/play/<int:song_id>")
def play_song(song_id):
    song = Song.query.get_or_404(song_id)
    return send_file(song.mp3_path, mimetype="audio/mpeg")


# -----------------------------
# Get users
# -----------------------------
@app.route("/users")
def get_users():
    users = User.query.limit(20).all()

    return jsonify([
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ])

# ---------------------------------
# Search song by name
# ---------------------------------
@app.route("/songs/search")
def search_song():
    song_name = request.args.get("title")

    if not song_name:
        return jsonify({"error": "title query parameter required"}), 400

    songs = Song.query.filter(
        Song.title.ilike(f"%{song_name}%")
    ).all()

    if not songs:
        return jsonify({"message": "No songs found"}), 404

    return jsonify([
        {
            "id": s.id,
            "title": s.title,
            "artist": s.artist,
            "genre": s.genre,
            "mp3_path": s.mp3_path,
            "created_at": s.created_at,
        }
        for s in songs
    ])



if __name__ == "__main__":
    app.run(debug=True)