import json
import requests
import time

endpoint = "http://api.open-notify.org/iss-now.json"
parameters = {}

requestobj = requests.get(endpoint, params = parameters)

print(f"status code: #{requestobj.status_code}")
print(f"headers: #{requestobj.headers}")

resultstring = requestobj.text

print(resultstring)

print()
resultdict = json.loads(resultstring)

print(resultdict.keys())
print(resultdict["timestamp"])

outfile = open("issposition.csv", "w")
number = 250
delay = 5
for i in range(0, number):
    requestobj = requests.get(endpoint, params=parameters)
    resultstring = requestobj.text
    resultdict = json.loads(resultstring)
    print(f"{resultdict['iss_position']['longitude']}, {resultdict['iss_position']['latitude']}", file=outfile)
    outfile.flush() #forces writing to file every time
    print(f"{i + 1} out of {number}")
    time.sleep(delay)

outfile.close()
