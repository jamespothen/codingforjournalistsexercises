animalsdict = {"dog": "mammal", "cat": "mammal", "turtle": "reptile"}

print(animalsdict)

print(animalsdict["dog"])
print(animalsdict["turtle"])

animalsdict["frog"] = "amphobian"

print(animalsdict["frog"])
print(animalsdict)

animalsdict["frog"] = "amphibian"

print(animalsdict["frog"])
print(animalsdict)

print(animalsdict.keys())
print(animalsdict.values())

print()

for animal in animalsdict.keys():
    print(f"A {animal} is a {animalsdict[animal]}")

print(f"Length is {len(animalsdict)}.")
