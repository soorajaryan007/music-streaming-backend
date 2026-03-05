import os
import uuid
from dotenv import load_dotenv

load_dotenv()

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")


def save_audio_file(file):

    filename = str(uuid.uuid4()) + ".mp3"

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(file_path)

    return file_path


    