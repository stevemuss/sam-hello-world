import json

def lambda_handler(event, context):
    print("I work!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }