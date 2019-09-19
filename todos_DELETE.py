import requests
import json

url = 'http://jsonplaceholder.typicode.com/todos'
payload = {'id': '200'}
r = requests.delete(url, data=json.dumps(payload))
json_response = r.json()
print(json_response)

#response is {} which means it has been deleted
#would return a 404 since that entry would not exist anymore
