import os
import uuid
import boto3
from dotenv import load_dotenv

load_dotenv()

STORAGE_TYPE = os.getenv("STORAGE_TYPE")

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
BUCKET_NAME = os.getenv("S3_BUCKET")

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION")
)


def save_audio_file(file):

    filename = str(uuid.uuid4()) + ".mp3"

    # LOCAL STORAGE
    if STORAGE_TYPE == "local":

        file_path = os.path.join(UPLOAD_FOLDER, filename)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file.save(file_path)

        return file_path

    # S3 STORAGE
    elif STORAGE_TYPE == "s3":

        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            filename,
            ExtraArgs={"ContentType": "audio/mpeg"}
        )

        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"

        return file_url