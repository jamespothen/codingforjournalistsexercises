keepgoing = True

sentence = ""

wordcount = 0

while keepgoing:
    newword = input("Please enter a word. Enter '.' to stop: ")
    wordcount += 1
    sentence += f" {newword}"
    if (newword == "."):
        keepgoing = False

print(sentence)
print(f"Number of words is {wordcount - 1}")
