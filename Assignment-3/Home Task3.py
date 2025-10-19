import math

number = int(input("Enter your number: "))
sum=0
isPerfect=False
for i in range(1,number,1):
    if number%i==0:
        sum+=i
if sum==number:
    isPerfect=True  

isPrime = True

if number <= 1:
    isPrime = False
else:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            isPrime = False
            break

if isPrime and isPerfect:
    print(number," is both Prime and Perfect number.")
elif isPrime:
    print(number," is Prime.")
elif isPerfect:
    print(number,"is perfect number")
else:
    print(number,"is neither prime nor perfect")