with open("Guest.txt","W") as dataFile:
    name=input("Enter your name:")
    dataFile.write(name)