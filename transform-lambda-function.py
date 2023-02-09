import requests
import boto3
import json 
import csv

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    bucket ='weatherbuk'
    response = s3.list_objects_v2(Bucket=bucket, Prefix='extract/')
    all = response['Contents']        
    latest = max(all, key=lambda x: x['LastModified'])
    key=latest['Key']
    
    data = s3.get_object(Bucket=bucket, Key=key)
    file_content = data['Body'].read().decode('utf-8')
    json_dict = json.loads(file_content)
    result_list=[]
    for i in json_dict:
        row_d = {}
        row_d["name"] = i['location']['name']
        row_d["region"] = i['location']['region']
        row_d["country"] = i['location']['country']
        row_d["tz_id"] = i['location']['tz_id']
        row_d["localtime"] = i['location']['localtime']
        row_d["temp_c"] = i['current']['temp_c']
        row_d["condition"] = i['current']['condition']['text']
        row_d["wind_mph"] = i['current']['wind_mph']
        row_d["feelslike_c"] = i['current']['feelslike_c']
    
        result_list.append(row_d)
        
    location = result_list[0]['localtime']
    file_name = "data"+location+".csv"
    target_file_path = "transform/" + file_name
    bucket = "weatherbuk" 
    
    with open('/tmp/data.csv', 'w', newline='') as file:
        
        fieldnames = ['name', 'region', 'country', 'tz_id', 'localtime', 'temp_c', 'condition', 'wind_mph', 'feelslike_c']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    
        writer.writeheader()
        for row in result_list:
            writer.writerow(row)
        
    
    #upload the data into s3
    s3.upload_file('/tmp/data.csv', bucket, target_file_path)
