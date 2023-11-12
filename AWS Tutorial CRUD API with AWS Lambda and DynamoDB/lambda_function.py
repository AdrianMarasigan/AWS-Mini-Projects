import boto3

dynamo = boto3.client('dynamodb')


def handler(event, context):
    body = None
    statusCode = 200
    headers = {
        "Content-Type": "application/json"
    }
    try:
        routeKey = event['routeKey']
        if routeKey == "DELETE /items/{id}":
            dynamo.delete_item(
                TableName="http-crud-tutorial-items",
                Key={
                    'id': event['pathParameters']['id']
                }
            )
            body = f"Deleted item {event['pathParameters']['id']}"
        elif routeKey == "GET /items/{id}":
            response = dynamo.get_item(
                TableName="http-crud-tutorial-items",
                Key={
                    'id': event['pathParameters']['id']
                }
            )
            body = response['Item']
        elif routeKey == "GET /items":
            response = dynamo.scan(
                TableName="http-crud-tutorial-items"
            )
            body = response['Items']
        elif routeKey == "PUT /items":
            requestJSON = json.loads(event['body'])
            dynamo.put_item(
                TableName="http-crud-tutorial-items",
                Item={
                    'id': requestJSON['id'],
                    'price': requestJSON['price'],
                    'name': requestJSON['name']
                }
            )
            body = f"Put item {requestJSON['id']}"
        else:
            raise Exception(f"Unsupported route: \"{routeKey}\"")
    except Exception as e:
        statusCode = 500
        body = str(e)

    return {
        'statusCode': statusCode,
        'headers': headers,
        'body': body
    }
