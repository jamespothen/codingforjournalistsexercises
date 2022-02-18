bottles = 99

while bottles >= 0:
    if bottles > 0:
        print(f"{bottles} bottles of beer on the wall...")
    else:
        print("No bottles of beer on the wall...")
    bottles -= 1  # equivalent to bottles = bottles - 1

print("Goodbye!")

print()

keepgoing = True

while keepgoing:
    print("I'm working")
    ans = input("Do you want to quit? (Y/N) ")
    if (ans == "Y") or (ans == "y"):
        print("Finished.")
        keepgoing = False

print("Goodbye again!")
