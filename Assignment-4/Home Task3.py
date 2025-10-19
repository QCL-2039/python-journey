myString=input("Enter your string:")
len_String=len(myString)

finalString=myString[1:]
ascii_value_of_last_char=ord(myString[len_String-1])
finalString+=chr(ascii_value_of_last_char+1)
print(finalString)
