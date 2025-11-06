def sum(*a):
    sum=0
    print("Sum of these numbers:")
    for i in a:
        sum+=i
    print(sum)

def sub(*a):
    sum=0
    print("Subtraction of these numbers:")
    for i in a:
        sum-=i
    print(sum)    
def multi(*a):
    result=1
    print("Multiplication of these numbers:")
    for i in a:
        result*=i
    print(result)

print("Module import successfully!")