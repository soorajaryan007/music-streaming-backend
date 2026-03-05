import os
from dotenv import load_dotenv

load_dotenv()

STORAGE_TYPE = os.getenv("STORAGE_TYPE", "local")

if STORAGE_TYPE == "s3":
    from storage.s3_storage import save_audio_file
else:
    from storage.local_storage import save_audio_file