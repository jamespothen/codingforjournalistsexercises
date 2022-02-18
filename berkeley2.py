import sodapy

website = "data.cityofberkeley.info"
dataset = "7ykt-c32j"

api = sodapy.Socrata(website, None)  # None is the place for a password

resultlist = api.get(dataset, height="5 Ft. 8 In.", limit=1000)

fieldlist = ["subject", "race", "statute_description", "height"]

for bookingdict in resultlist:
    for field in fieldlist:
        if field in bookingdict.keys():
            print(f"{field}: {bookingdict[field]}")
        else:
            print(f"{field} unknown")
    print()
