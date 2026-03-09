import os
import uuid
from config import Config


class LocalStorage:

    def __init__(self):
        self.upload_folder = Config.UPLOAD_FOLDER
        os.makedirs(self.upload_folder, exist_ok=True)

    def save_audio_file(self, file):

        filename = f"{uuid.uuid4()}.mp3"

        file_path = os.path.join(self.upload_folder, filename)

        file.save(file_path)

        return file_path
    