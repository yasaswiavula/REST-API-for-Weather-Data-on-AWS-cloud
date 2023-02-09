import requests
import json

# 10 cities cities- New York, Seattle, Winter Garden, Katy, Los Angeles, Washington
# Arnold, Cincinnati, Elk Grove Village, Mount Pleasant

API = "https://85bx4xrtuc.execute-api.us-east-2.amazonaws.com/prod/city?name=New York"
response = requests.get(API)
resp = json.loads(response.content)
print("API response- ")
for i in resp:
    print(i,": ", resp[i])

API2 = "https://85bx4xrtuc.execute-api.us-east-2.amazonaws.com/prod/city?name=Mount Pleasant"
response = requests.get(API2)
resp = json.loads(response.content)
print("\nAPI2 response- ")
for i in resp:
    print(i,": ", resp[i])
