import boto3
import json

athena_client = boto3.client('athena')


def lambda_handler(event, context):
    for record in event['Records']:
        key = record['s3']['object']['key']
        bucket = record['s3']['bucket']['name']

        query = f"SELECT * FROM class_demographics user_id = 'class_name';"

        response = athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': 'diablo4'
            },
            ResultConfiguration={
                'OutputLocation': f"s3://{bucket}/query_results/"
            }
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Query execution started successfully!')
    }
