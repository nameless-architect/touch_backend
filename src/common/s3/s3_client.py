import boto3

from common.s3.s3_config import S3Config


class S3Client:

    def __init__(self):
        s3_config = S3Config()
        s3 = boto3.resource(
            service_name='s3',
            region_name='us-east-2',
            aws_access_key_id=s3_config.get_access_key_id(),
            aws_secret_access_key=s3_config.secret_access_key()
        )
        self._s3 = s3

    def get_file_object(self, data):

        def callback(*args, **kwargs):
            print(args)
            print(kwargs)
        bucket = self._s3.Bucket('touchprofilepic')
        bucket.download_fileobj('sample_1280x720_surfing_with_audio.mp4', data, Callback=callback)

    def upload_file_to_bucket(self, file, file_name: str, bucket_name: str = 'touchprofilepic'):
        self._s3.upload_fileobj(file, bucket_name, file_name)


