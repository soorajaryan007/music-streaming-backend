from models import Song,User, db
from cache.redis_cache import RedisCache
from repositories.song_repository import SongRepository



class SongService:

    def __init__(self):
        self.song_repo = SongRepository()
        self.redis_cache = RedisCache()

    def get_all_songs(self):
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

    def get_all_users(self):
        users = User.query.limit(20).all()

        return [
            {"id": u.id, "username": u.username, "email": u.email}
            for u in users
        ]

    def get_song_by_title(self, song_name):

        songs = Song.query.filter(
            Song.title.ilike(f"%{song_name}%")
        ).all()

        if not songs:
            return None

        return [
            {
                "id": s.id,
                "title": s.title,
                "artist": s.artist,
                "genre": s.genre,
                "mp3_path": s.mp3_path,
                "created_at": s.created_at,
            }
            for s in songs
        ]

    def get_song_id(self, song_id):
        song = db.session.get(Song, song_id)
        return song

    def create_song(self, title, artist, genre, mp3_path):

        song = Song(
            title=title,
            artist=artist,
            genre=genre,
            mp3_path=mp3_path
        )

        db.session.add(song)
        db.session.commit()

        return song

    def get_song_url(self, song_id):

        cache_key = f"song:{song_id}"

        cached_song = self.redis_cache.get(cache_key)

        if cached_song:
            print("Cache HIT")
            return cached_song

        print("Cache MISS")

        song = self.song_repo.get_song_by_id(song_id)

        if not song:
            return None

        self.redis_cache.set(cache_key, song.mp3_path)

        return song.mp3_path