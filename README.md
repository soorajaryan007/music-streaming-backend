# 🎧 Spotify Clone (Phase 1)

A minimal backend prototype of a Spotify-like music service built with **Flask**, **PostgreSQL**, and **SQLAlchemy**.

This project is intentionally simple and designed as the **foundation for future scaling** (Redis, CDN, Load Balancer, Kafka, etc.).

---

# 🚀 Features

* Flask REST API
* PostgreSQL database
* SQLAlchemy ORM
* 100 dummy users (auto-seeded)
* 10 demo songs (local MP3)
* Basic music streaming endpoint
* Clean, scalable project structure

---

# 🏗️ Current Architecture (Phase 1)

```
Client → Flask API → PostgreSQL
                 → Local MP3 files
```

**Not included yet (planned later):**

* ❌ Redis caching
* ❌ CDN
* ❌ Load balancer
* ❌ Kafka
* ❌ Microservices

---

# 📁 Project Structure

```
spotify_clone/
│
├── app.py
├── config.py
├── models.py
├── seed.py
├── requirements.txt
└── songs/
    └── song1.mp3 ... song10.mp3
```

---

# ⚙️ Prerequisites

Make sure you have installed:

* Python 3.10+
* PostgreSQL
* pip
* virtualenv (recommended)

---

# 🔧 Setup Instructions

## 1️⃣ Clone or create project

```bash
mkdir spotify_clone
cd spotify_clone
```

---

## 2️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
```

Windows:

```bash
.venv\\Scripts\\activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create PostgreSQL database

Open psql and run:

```sql
CREATE DATABASE spotify_clone;
```

---

## 5️⃣ Configure database (IMPORTANT)

Edit **config.py** if your credentials differ:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/spotify_clone"
```

---

## 6️⃣ Add MP3 files

Create folder:

```bash
mkdir songs
```

Add files:

```
song1.mp3
song2.mp3
...
song10.mp3
```

⚠️ Use small dummy audio files for testing.

---

## 7️⃣ Seed the database

This will create:

* ✅ Tables
* ✅ 100 dummy users
* ✅ 10 songs

Run:

```bash
python seed.py
```

Expected output:

```
Database seeded!
```

---

## 8️⃣ Run the server

```bash
python app.py
```

Server runs at:

```
http://localhost:5000
```

---

# 🧪 API Endpoints

## Health Check

```
GET /
```

Response:

```json
{
  "message": "Spotify Clone Running 🎵"
}
```

---

## Get All Songs

```
GET /songs
```

Returns list of available songs.

---

## Play Song

```
GET /play/<song_id>
```

Example:

```
http://localhost:5000/play/1
```

Streams the MP3 file.

---

## Get Users (sample)

```
GET /users
```

Returns first 20 users.

---

# 🗃️ Database Schema

## Users Table

| Column     | Type         |
| ---------- | ------------ |
| id         | Integer (PK) |
| username   | String       |
| email      | String       |
| created_at | DateTime     |

## Songs Table

| Column     | Type         |
| ---------- | ------------ |
| id         | Integer (PK) |
| title      | String       |
| artist     | String       |
| genre      | String       |
| mp3_path   | String       |
| created_at | DateTime     |

---

# 🔮 Future Roadmap

Planned upgrades toward production scale:

* Redis caching layer
* CDN for audio delivery
* Load balancer
* Kafka event streaming
* User playlists
* Authentication & JWT
* Recommendation engine
* Microservices split

---

# 🧠 Learning Goal

This project is meant to help understand:

* Backend architecture basics
* Media streaming flow
* Database design
* How Spotify-like systems evolve step by step

---

# 👨‍💻 Author

Sooraj Aryan

---

**Next milestone:** scaling phase with caching and performance improvements 🚀
