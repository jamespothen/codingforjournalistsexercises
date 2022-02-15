mylist = ["Monday", "Tuesday", "Wednesday", "Thursday"]
print(len(mylist))
print(mylist)
print(mylist[1]) #pulling out an element of a list is a string
print(mylist[1:2]) #['Tuesday']
print(mylist[2:]) #slicing a list is still a list
print(mylist[:2]) #['Monday', 'Tuesday']

if "Monday" in mylist:
    print("We have a Monday.")
else:
    print("No Monday.")

if "Fooday" in mylist:
    print("We have a Fooday.")
else:
    print("No Fooday.")

# if answer in ["Y", "y", "N", "n"]:

mylist.append("Friday")
print(mylist)

mylist.append("Sitterday")
print(mylist)

lastelement = mylist.pop()
print(mylist)
print(f"Last element in list was {lastelement}.")

print()

mylist.insert(3, "Dogday")
print(mylist)

mylist.remove("Dogday")
print(mylist)

mylist.append("Fooday")
mylist.insert(0, "Fooday")
print(mylist)

print()
print(f"Monday is element number {mylist.index('Monday')}")
print(f"Fooday is element number {mylist.index('Fooday')}")

print(f"There are {mylist.count('Fooday')} 'Foodays'")
mylist.remove("Fooday")
print(mylist)
print()

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)
