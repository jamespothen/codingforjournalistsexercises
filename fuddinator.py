print("Welcome to the Fudd-inator! 🐰")
print()
sentence = input("Please input a sentence: ")
print()

count = 0
newsentence = ""

for letter in sentence:
    if (letter == "r"):
        count += 1
        newsentence += "w"
    elif(letter == "R"):
        count += 1
        newsentence += "W"
    else:
        newsentence += letter

print(f"The number of r's is {count}")
print(f"Elmer Fudd would say: {newsentence}")
print()
print("Goodbye! 👋🏽")
