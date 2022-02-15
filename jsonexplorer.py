import json

studentdict = {"nid":"N123456789",
               "name":"Andy Hamilton",
               "address":{"street":"123 Fake Street",
                          "state":"New York",
                          "zip":10003},
               "classes":["Programming", "Basket Weaving", "Fundraising"]
               }

classeslist = studentdict["classes"]

for course in classeslist:
    print(course)

print(studentdict["nid"])

print()

studentstring = json.dumps(studentdict)

print(studentstring)

# print(studentstring["nid"])

newdict = json.loads(studentstring)

print(newdict["nid"])
