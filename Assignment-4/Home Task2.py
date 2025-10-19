myString=input("Enter your string:")

length=myString.find(",")
firstString=myString[:length]
secondString=myString[length+1::]
min_lenth=min(len(firstString),len(secondString))
finalString=""

for i in range(min_lenth):
    finalString+=firstString[i]+secondString[i]

finalString+=firstString[min_lenth:]+secondString[min_lenth:]
print(firstString)
print(secondString)
print(finalString)