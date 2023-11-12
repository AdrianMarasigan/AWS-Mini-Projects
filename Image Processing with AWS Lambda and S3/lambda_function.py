import json
import boto3
from PIL import Image
import os
import uuid

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    for record in event['Records']:
        key = record['s3']['object']['key']
        bucket = record['s3']['bucket']['name']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/resized-{}'.format(key)

        s3_client.download_file(bucket, key, download_path)

        with Image.open(download_path) as image:
            image.thumbnail((128, 128))
            image.save(upload_path)

        s3_client.upload_file(upload_path, '{}-resized'.format(bucket), key)

        # Clean up
        os.remove(download_path)
        os.remove(upload_path)
