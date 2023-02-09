import boto3
import json
from boto3.dynamodb.conditions import Key

tableName = 'weather-table-data'
# define the DynamoDB table that Lambda will connect to

# create the DynamoDB resource
ddb = boto3.resource('dynamodb').Table(tableName)

print('Loading function')

def lambda_handler(event, context):
            
    resp = ddb.get_item(
            Key={
                'name' : event["queryStringParameters"]['name']
            }
        )
    Response = resp["Item"]
    #Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(Response)
    	
    return responseObject
    
    
