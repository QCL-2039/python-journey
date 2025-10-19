number=int(input("Enter your number:"))

while number>0:

    i=number%10
    number //=10
    print(i,end=",")