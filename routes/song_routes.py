from flask import Blueprint, jsonify, request, abort

from utils.response_handler import StreamingService
from api_latency.latency import measure_latency
from services.song_upload import SongController

from services.song_service import SongService

song_bp = Blueprint("songs", __name__)

u = SongController()
upload_song =u.upload_song

st = StreamingService()
stream_song = st.stream_song

s = SongService()
get_all_songs = s.get_all_songs
get_song_url = s.get_song_url
get_song_by_title = s.get_song_by_title

@song_bp.route("/songs")
def get_songs():
    songs = get_all_songs()
    return jsonify(songs)


@song_bp.route("/play/<int:song_id>")
@measure_latency
def play_song(song_id):
    song_url = get_song_url(song_id)

    if not song_url:
        abort(404)

    return stream_song(song_url)


@song_bp.route("/songs/search")
def search_song():
    song_name = request.args.get("title")

    if not song_name:
        return {"error": "title query parameter required"}, 400

    songs = get_song_by_title(song_name)

    if not songs:
        return {"message": "No songs found"}, 404

    return jsonify(songs)

@song_bp.route("/upload-song", methods=["POST"])
def upload_song_route():
    return upload_song()