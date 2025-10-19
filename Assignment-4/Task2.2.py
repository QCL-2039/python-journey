myString = input("Enter your String:")

for i in range(len(myString)):
    ch = myString[i]
    if i % 2 != 0 and 'a' <= ch <= 'z':   # Only convert lowercase letters
        ch = chr(ord(ch) - 32)
    print(ch, end="")
