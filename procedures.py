def getnumber(promptstring):
    keepgoing = True
    while keepgoing:
        numstring = input(promptstring)
        try:
            num = int(numstring)
            keepgoing = False
        except:
            print("That didn't work, please try again.")
    return num

### MAIN BODY ###

num1 = getnumber("A number please: ")
num2 = getnumber("Another num num: ")
print("The product is " + str(num1 * num2))
