keepgoing = True
phonenumberdict = {"John": "555-5555", "Susan": "222-2222"}

# Add mobile, address, etc.
# Create object with attributes and methods

while keepgoing:
    name = input("Please enter a name to get the corresponding number: ")
    if name in phonenumberdict.keys():
        print(phonenumberdict[name])
    else:
        newnumber = input("Name not found. Please enter their phone number: ")
        phonenumberdict[name] = newnumber

    goagain = input("Want to look up another number? (y/n)")
    keepgoing = False if goagain == "n" else True
    print()

print("Bye! 👋🏽")
