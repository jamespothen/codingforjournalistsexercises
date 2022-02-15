import json
import requests

endpoint = 'https://data.cityofberkeley.info/resource/7ykt-c32j.json'
parameters = {'$limit':10}

requestobj = requests.get(endpoint, params = parameters)

bookinglist = json.loads(requestobj.text)

for bookingdict in bookinglist:
    print(bookingdict['subject'])
    print(bookingdict['race'])
    print(bookingdict['statute_description'])
    print()
