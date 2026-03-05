from models import Song
from models import db

def get_song_by_id(song_id):
    return db.session.get(Song, song_id)