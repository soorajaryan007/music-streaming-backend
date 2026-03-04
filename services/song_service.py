from models import Song,User, db

def get_all_songs():
    songs = Song.query.all()

    return [
        {
            "id": s.id,
            "title": s.title,
            "artist": s.artist,
            "genre": s.genre,
        }
        for s in songs
    ]


def get_all_users():
    users = User.query.limit(20).all()

    return ([
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ])


def get_song_by_title(song_name):

    songs = Song.query.filter(
        Song.title.ilike(f"%{song_name}%")
    ).all()

    if not songs:
        return None

    return ([
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


def get_song_id(song_id):
    song = db.session.get(Song, song_id)
    return song




def create_song(title, artist, genre, mp3_path):

    song = Song(
        title=title,
        artist=artist,
        genre=genre,
        mp3_path=mp3_path
    )

    db.session.add(song)
    db.session.commit()

    return song