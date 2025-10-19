num=int(input("Enter your number:"))
count=0
i=1
while i<=num:
    if (num%i==0):
        print(i)
        count+=1
        i+=1
    else:
        i+=1
print("Total divisors:",count)        


