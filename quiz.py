print()
print("Which Ted Lasso character are you?")

teastr = input("Do you like tea? (y/n) ")
optimiststr = input("Are you an optimist? (y/n) ")

print()

if (teastr == "y") & (optimiststr == "y"):
    print("You are Becks!")
elif (teastr == "y") & (optimiststr == "n"):
    print("You are Roy!")
elif (teastr == "n") & (optimiststr == "y"):
    print("You are Ted!")
else:
    print("You are Beard!")
