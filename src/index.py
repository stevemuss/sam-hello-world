# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import json

def lambda_handler(event, context):
  dynamodb_client = boto3.client('dynamodb')
  
  data = json.loads(event.get("body"))

  if data:
    save_data = {
        'id': {'S': data.get("name", "")},
        'recommendation_type': {'S': data.get("recommendation_type", "")},
        'recommendation': {'S': data.get("recommendation", "")},
        'python_level': {'S': data.get("python_level", "")},
    }
    dynamodb_client.put_item(TableName='RecommendationsData', Item=save_data)
    print(f'I got data from: {data.get("name", "")}')
  
  return {
      'statusCode': 200,
      'body': json.dumps({
          'update': 'Successfully inserted data!',
          'message': f'Thanks for you recommendation {data.get("name", "")}'
        })
  }
