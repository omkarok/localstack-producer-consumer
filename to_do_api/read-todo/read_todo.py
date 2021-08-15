from __future__ import print_function

import json
import decimal
import os
import boto3
#from botocore.exceptions import ClientError


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


# Get the service resource.
os.environ['DYNAMODB_ENDPOINT_URL']='http://localhost:4566'
DYNAMODB_ENDPOINT_URL = os.environ.get("DYNAMODB_ENDPOINT_URL")
dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT_URL, region_name='us-east-1')

# set environment variable
TABLE_NAME = os.environ['TABLE_NAME']


def lambda_handler(event, context):
    table = dynamodb.Table('ToDoTable')
    to_do_list = []
    get_item = []
    to_do ={}
    if len(event) > 0:
        response= table.get_item(
            Key={
                'id' : event['uuid'],
            }
        )
        if 'Item' in response:
            print(response['Item'])
            print(json.dumps(response['Item'], cls=DecimalEncoder))
            task = json.dumps(response['Item'], cls=DecimalEncoder)
            to_do['task'] = task
            get_item.append(task)
        return {
            'statusCode': 200,
            'getitem': get_item
        }
    else: 
        # Scan items in table
        try:
            response = table.scan()
        except Exception as e:
            print(e)
        else:
            # print item of the table - see CloudWatch logs
            for i in response['Items']:
                print(json.dumps(i, cls=DecimalEncoder))
                tasks = json.dumps(i, cls=DecimalEncoder)
                to_do['tasks'] = tasks
                to_do_list.append(tasks)

        return {
            'statusCode': 200,
            'to_do': to_do_list,
        }