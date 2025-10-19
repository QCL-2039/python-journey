myString=input("Enter your string:")
finalString=""

isUpper=ord(myString[0])

if isUpper>=65 and isUpper<=90:
    for i in range(len(myString)):
            if i%2==0:
             finalString+=myString[i].upper()
            else:
                finalString+=myString[i].lower()
else:
    for i in range(len(myString)):
            if i%2==0:
             finalString+=myString[i].lower()
            else:
                finalString+=myString[i].upper()                
print(finalString)         
      