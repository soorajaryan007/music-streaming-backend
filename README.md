
## 🎧 Music Streaming App

A scalable backend prototype of a **Spotify-like music streaming service** built using **Flask, PostgreSQL, and SQLAlchemy**.

This project implements a backend system responsible for **user management, song metadata storage, and audio streaming**.
It is intentionally designed as a **clean foundational architecture** that can later scale using technologies such as **Redis, CDN, Kafka, and microservices**.

---

# 🏗 Architecture Overview

The system is designed as a modular backend service that manages music metadata and audio delivery.

### Core Responsibilities

* User management
* Song metadata storage
* Music discovery APIs
* Audio streaming

### System Flow

```
Users
   ↓
Application Load Balancer
   ↓
EC2 Instance 1 (Gunicorn Flask)
EC2 Instance 2 (Gunicorn Flask)
   ↓
Redis (ElasticCache)
   ↓
PostgreSQL / Database
```

### Planned Future Architecture

```
Users
   ↓
Application Load Balancer
   ↓
EC2 Instance 1 (Gunicorn Flask)
EC2 Instance 2 (Gunicorn Flask)
   ↓
Redis (ElasticCache)
   ↓
PostgreSQL / Database
```

This architecture mirrors the **evolution path of real streaming platforms**.

---

# 🚀 Features

* REST API built with Flask
* PostgreSQL relational database
* SQLAlchemy ORM for database abstraction
* Automatic database seeding
* 100 dummy users for testing
* 10 demo songs stored locally
* Audio streaming endpoint
* Clean modular backend structure

---

# 🧰 Tech Stack

Backend Framework
**Flask**

Database
**PostgreSQL**

ORM
**SQLAlchemy**

Programming Language
**Python**

API Testing
**Postman / Curl**

Version Control
**Git**

Future Infrastructure (Planned)

* Redis
* AWS S3
* CDN
* Kafka
* Load Balancer

---

# 📁 Project Structure

```
spotify_clone/
│
├── app.py              # Flask application entry point
├── config.py           # Environment configuration
├── models.py           # SQLAlchemy database models
├── seed.py             # Database seeding script
├── requirements.txt    # Python dependencies
│
└── songs/              # Local audio storage
    ├── song1.mp3
    ├── song2.mp3
    └── song10.mp3
```

This structure keeps **application logic separated from configuration and data initialization**.

---

# 🔌 API Endpoints

### Health Check

```
GET /
```

Response

```json
{
  "message": "Spotify Clone Running 🎵"
}
```

### Search Songs

```
POST /
```

Response

```json
[
  {
    "artist": "Yash",
    "created_at": "Thu, 05 Mar 2026 10:49:26 GMT",
    "genre": "Rock",
    "id": 10,
    "mp3_path": "https://music-songs-list.s3.amazonaws.com/89f544e0-ca5f-4445-a42b-93af0acbe3f8.mp3",
    "title": "Tabaahi Toxic"
  }
]
```

---

### Get All Songs

```
GET /songs
```

Returns metadata for all available songs.

---

### Stream Song

```
GET /play/<song_id>
```

Example

```
http://localhost:5000/play/1
```

Streams the requested MP3 file.

---

### Get Users (Sample)

```
GET /users
```

Returns the first 20 users from the database.

---

# 🗄 Database Schema

### Users Table

| Column     | Type                  |
| ---------- | --------------------- |
| id         | Integer (Primary Key) |
| username   | String                |
| email      | String                |
| created_at | DateTime              |

---

### Songs Table

| Column     | Type                  |
| ---------- | --------------------- |
| id         | Integer (Primary Key) |
| title      | String                |
| artist     | String                |
| genre      | String                |
| mp3_path   | String                |
| created_at | DateTime              |

---

# ⚙️ Setup Instructions

## 1. Clone the Repository

```
git clone https://github.com/yourusername/spotify_clone.git
cd spotify_clone
```

---

## 2. Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate
```

## 2. Create .env

```
DATABASE_URL=postgresql://user:sooraj7972@localhost:5433/spotify_clone
S3_BASE_URL = "songs"
FLASK_ENV=development
ENV=local
UPLOAD_FOLDER="songs"

STORAGE_TYPE=local
S3_BUCKET=my-music-bucket
AWS_REGION=ap-south-1
AWS_ACCESS_KEY=xxxx
AWS_SECRET_KEY=xxxx
```

Windows

```
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Create PostgreSQL Database

Open PostgreSQL and run:

```sql
CREATE DATABASE spotify_clone;
```

---

## 5. Configure Environment Variables

Create a `.env` file in the project root:

```
DATABASE_URL=postgresql://user:password@localhost:5433/db_name
S3_BUCKET=my-local-bucket
FLASK_ENV=development
```

If needed, adjust `config.py`:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/spotify_clone"
```

---

## 6. Add Demo Audio Files

Create folder:

```
songs/
```

Add test files:

```
song1.mp3
song2.mp3
...
song10.mp3
```

Use **small MP3 files for testing**.

---

## 7. Seed the Database

This will create:

* Database tables
* 100 dummy users
* 10 demo songs

Run:

```
python seed.py
```

Expected output:

```
Database seeded!
```

---

## 8. Run the Server

```
python app.py
```

Server runs at:

```
http://localhost:5000
```

---



# ☁ Deployment

The project is designed to be deployable on cloud infrastructure such as AWS.

Typical deployment stack:

* **AWS EC2** – application hosting
* **PostgreSQL / RDS** – database
* **Amazon S3** – audio storage
* **Nginx** – reverse proxy
* **Gunicorn** – production WSGI server

---

# 🔮 Future Improvements

Planned improvements to evolve the system toward **production-scale architecture**:

* Redis caching layer
* CDN integration for faster audio delivery
* Load balancing for horizontal scaling
* Kafka event streaming
* User playlists
* JWT authentication
* Music recommendation engine
* Microservices architecture

---

# 🎯 Learning Goals

This project demonstrates:

* Backend system architecture
* REST API design
* Database schema modeling
* Media streaming basics
* Building scalable backend foundations

---

# 👨‍💻 Author

**Sooraj Aryan**

---

# 📄 License

MIT License

