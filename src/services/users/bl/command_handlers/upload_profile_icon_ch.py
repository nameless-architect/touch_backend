from fastapi import UploadFile

from common.s3.s3_client import S3Client


class UploadProfileIconCH:
    def __init__(self, s3_client: S3Client):
        self._s3_client = s3_client

    def do_logic(self, file: UploadFile):
        self._s3_client.upload_file_to_bucket(file.file, file.filename)

    @classmethod
    def construct(cls):
        s3_client = S3Client()
        return cls(s3_client)
