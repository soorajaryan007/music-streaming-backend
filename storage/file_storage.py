import os
import uuid

UPLOAD_FOLDER = "songs"

def save_audio_file(file):

    filename = str(uuid.uuid4()) + ".mp3"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(file_path)

    return file_path