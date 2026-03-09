from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENV = os.getenv("ENV", "local")

    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")

    STORAGE_TYPE = os.getenv("STORAGE_TYPE", "local")
    
    # S3 configuration
    S3_BUCKET = os.getenv("S3_BUCKET")
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    AWS_REGION = os.getenv("AWS_REGION")