import requests
import boto3
import json

s3 = boto3.client('s3')
  
def lambda_handler(event, context):
   
   json_dict = []
   city_zips = [48858, 60007, 10001, 98101 , 20022, 77494, 34787, 90011, 63010, 45202]
   bucket ='weatherbuk'
   
   for i in city_zips:
      api_response = requests.get('http://api.weatherapi.com/v1/current.json?key=c5ae450f0fb041bd94d175330231901&q='+str(i)+'&aqi=no')
      json_dict.append(json.loads(api_response.text))
   location = str(json_dict[0]['location']['localtime'])
   
   
   
   data=json.dumps(json_dict)
   print(data)
   fileName = 'data' + location + '.json'
   uploadByteStream = bytes(data.encode('utf-8'))
   s3.put_object(Bucket=bucket, Key="extract/"+fileName, Body=uploadByteStream)
   print('Put Complete') 
