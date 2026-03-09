from flask import request, jsonify
from services.song_service import SongService
from storage.storage_factory import StorageFactory


class SongController:

    def __init__(self):
        self.song_service = SongService()
        self.storage = StorageFactory()

    def upload_song(self):

        file = request.files.get("file")
        title = request.form.get("title")
        artist = request.form.get("artist")
        genre = request.form.get("genre")

        if not file:
            return {"error": "No file uploaded"}, 400

        file_path = self.storage.save_audio_file(file)

        song = self.song_service.create_song(
            title,
            artist,
            genre,
            file_path
        )

        return jsonify({
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "genre": song.genre
        })