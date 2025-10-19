myString=input("Enter your string:")
index=int(input("Enter the index no.:"))

new_String=myString[index::-1]+myString[index+1::]
print(new_String)