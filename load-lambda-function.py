import json
import boto3
import csv 
import codecs

# name	region	country	tz_id	localtime	temp_c	condition	wind_mph	feelslike_c
def lambda_handler(event, context):
    # TODO implement
    region = 'us-east-2'
    
    s3 = boto3.client('s3')
    bucket ='weatherbuk'
    response = s3.list_objects_v2(Bucket=bucket, Prefix='transform/')
    all = response['Contents']        
    latest = max(all, key=lambda x: x['LastModified'])
    file_key=latest['Key']
    
    ddb = boto3.resource("dynamodb", region_name = region)
    table = ddb.Table('weather-table-data')
    
    data = s3.get_object(Bucket=bucket, Key=file_key)

    for row in csv.DictReader(codecs.getreader("utf-8")(data["Body"])):
        table.put_item(Item = row)
