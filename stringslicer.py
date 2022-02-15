teststring = "It was the best of times. It was the worst of times."

print(f"Here's a slice: {teststring[0:5]}")

print(f"Here's another: {teststring[7:]}")
print(f"Here's another: {teststring[:9]}")
print(f"The string length is {len(teststring)}")

mystring = input("Please give me a string: ")
newstring = mystring.replace("t", "+")
print(newstring)

newstring = mystring.replace(" ", "_")
print(newstring)

newstring = mystring.replace(" ", "")
print(newstring)

newstring = mystring.lower()
print(newstring)

newstring = mystring.upper()
print(newstring)

newstring = mystring.strip()
print(newstring)

index = mystring.find("ex")
print(f"ex is found at position {index}")
print(mystring[index:])

print("Okay I ❤️  you! Bye Bye!")
