# Option 1: Using Response and the built in methods with Requests to get the data from JSON site
#I liked this one the most, more concise but I wanted to include the other showing more python/json work/conversion
import requests
import pprint

r = requests.get('http://jsonplaceholder.typicode.com/todos')
# The response is a list of 200 todos
pprint.pprint(r.json())
