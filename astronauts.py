import json
import requests

endpoint = "http://api.open-notify.org/astros.json"
parameters = {}

requestobj = requests.get(endpoint, params=parameters)

resultstring = requestobj.text

resultdict = json.loads(resultstring)

print(f"There are {resultdict['number']} people in space.")

print("Their names are: ")

peopledict = resultdict["people"]

for person in peopledict:
    print(f"{person['name']}")
