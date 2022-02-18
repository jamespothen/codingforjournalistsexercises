def changestuff(number, phrase, collection):
    number += 1
    phrase += " The end."
    collection.append("I'm done.")
    print("Inside changestuff. My variables are: ")
    print(number)
    print(phrase)
    print(collection)
    return


### MAIN BODY ###

num = 20
phr = "I'm changing"
coll = ["Alpha", "Beta", "Gamma"]
print("Our starting variables are")
print(num)
print(phr)
print(coll)
print()

changestuff(num, phr, coll)
print()

print("Our final values are")
print(num)
print(phr)
print(coll)
