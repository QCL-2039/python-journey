with open("Test.txt","r") as f:
    data=f.read()
word=input("Enter your word to be searched:")    

if word in data:
    print(word,"is found.")
else:
    print(word," not found")