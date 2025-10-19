myString = input("Enter your string: ")
isBinary = True 

for i in range(len(myString)):
    if myString[i] != "0" and myString[i] != "1":
        isBinary = False
        break 

if isBinary:
    print("Binary Number")
else:
    print("Not Binary")
