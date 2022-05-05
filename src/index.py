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
    dynamodb_client.put_item(TableName='WeatherData', Item=save_data)
  
  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }
