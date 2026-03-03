import random
from faker import Faker
from app import app
from models import db, User, Song

fake = Faker()

SONG_FILES = [
    "songs/song1.mp3",
    "songs/song2.mp3",
    "songs/song3.mp3",
    "songs/song4.mp3",
  
]


def seed_users():
    print("Seeding users...")
    for _ in range(100):
        user = User(
            username=fake.user_name() + str(random.randint(1, 9999)),
            email=fake.email(),
        )
        db.session.add(user)


def seed_songs():
    print("Seeding songs...")
    for i in range(4):
        song = Song(
            title=f"Demo Song {i+1}",
            artist=f"Artist {i+1}",
            genre=random.choice(["Pop", "Rock", "Jazz", "HipHop"]),
            mp3_path=SONG_FILES[i],
        )
        db.session.add(song)


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

        seed_users()
        seed_songs()

        db.session.commit()
        print("✅ Database seeded!")