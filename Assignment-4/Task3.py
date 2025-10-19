# Sohel-Rana-Bhuiyan
myString=input("Enter your string:")
split_char=input("Enter your splitting character:")
newString=""
for i in range(len(myString)):

    if myString[i]== split_char:
        print(newString)
        newString=""
    else:
        newString+=myString[i]
        
if newString:
    print(newString)  
