import random
from faker import Faker
from app import app
from models import db, User, Song
from dotenv import load_dotenv
import os

load_dotenv()


S3_BASE_URL = os.getenv("S3_BASE_URL")
fake = Faker()


SONG_FILES = [
    f"{S3_BASE_URL}/song1.mp3",
    f"{S3_BASE_URL}/song2.mp3",
    f"{S3_BASE_URL}/song3.mp3",
    f"{S3_BASE_URL}/song4.mp3",
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