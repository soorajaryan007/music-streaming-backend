from flask import request, jsonify
from services.song_service import SongService
from storage.storage_factory import save_audio_file
s = SongService()
creat_song = s.create_song
def upload_song():

    file = request.files.get("file")
    title = request.form.get("title")
    artist = request.form.get("artist")
    genre = request.form.get("genre")

    if not file:
        return {"error": "No file uploaded"}, 400

    file_path = save_audio_file(file)

    song = create_song(title, artist, genre, file_path)

    return jsonify({
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre
    })