from config import Config


class StorageFactory:

    def __init__(self):
        if Config.STORAGE_TYPE == "s3":
            from storage.s3_storage import S3Storage
            self.storage = S3Storage()
        else:
            from storage.local_storage import LocalStorage
            self.storage = LocalStorage()

    def save_audio_file(self, file):
        return self.storage.save_audio_file(file)