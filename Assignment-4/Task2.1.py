myString=input("Enter your string:")

for i in range(len(myString)):
    print(f"{myString[i]}:{ord(myString[i])}")