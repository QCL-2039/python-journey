
a=int(input("Enter the number series to be expanded:"))
sum=0
for i in range (1,a+1,1):
    if i % 2 !=0:
        sum+= pow(i,2)
    else:
        sum-= pow(i,2)
print(sum)
