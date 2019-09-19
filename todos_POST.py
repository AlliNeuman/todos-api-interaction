import requests
import json

url = 'http://jsonplaceholder.typicode.com/todos'
payload = {'userId': '18', 'id': '201', 'title': 'finish code challenge', 'completed': 'false'}
r = requests.post(url, data=json.dumps(payload))
# verify the post was created
print(r.status_code)
