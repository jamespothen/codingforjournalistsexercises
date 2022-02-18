namestr = input("What is your name? ")
agestr = input("How old are you? ")
ageint = int(agestr)
if ageint >= 21:
    print(f"Hello {namestr}, let me buy you a drink")
elif ageint >= 18:
    print("Can't buy you a drink.")
    print("But I'd like to chat.")
else:
    print("You're too young to drink.")
    print("Nice try.")

print("Can I borrow ten bucks?")
