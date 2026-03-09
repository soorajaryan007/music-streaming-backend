import uuid
import boto3
from config import Config


class S3Storage:

    def __init__(self):
        self.bucket = Config.S3_BUCKET

        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=Config.AWS_ACCESS_KEY,
            aws_secret_access_key=Config.AWS_SECRET_KEY,
            region_name=Config.AWS_REGION
        )

    def save_audio_file(self, file):

        filename = f"{uuid.uuid4()}.mp3"

        self.s3.upload_fileobj(
            file,
            self.bucket,
            filename,
            ExtraArgs={"ContentType": "audio/mpeg"}
        )

        file_url = f"https://{self.bucket}.s3.amazonaws.com/{filename}"

        return file_url