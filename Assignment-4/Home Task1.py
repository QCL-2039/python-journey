myString = input("Enter your String: ")
newString = myString[0]  # start with the first character

for i in range(1, len(myString)):
    if myString[i] != myString[i - 1]:
        newString += myString[i]

print(newString)
