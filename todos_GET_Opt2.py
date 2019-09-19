import json
import requests
import pprint

r = requests.get('http://jsonplaceholder.typicode.com/todos')
#the response is a class model from Response
# print(type(r))
#We can run different methods on this to pull the different data we want
#running json on it delivers us a list of the 200 todos
# print(type(r.json()))

#data encoded is turned into a string
data_encoded = json.dumps(r.json())
# print(type(data_encoded))
#then it is converted back to a list.
data = json.loads(data_encoded)
print(data)
