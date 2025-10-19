import math

def special_sum(n):
    perfect_sum=0
    
    for i in range(1,n+1):
        sum=0
        for j in range(1,i):
            if i % j==0:
                sum+=j
        if i==sum:
          
          perfect_sum+=i          
   
    prime_sum=0
    for i in range(2, n + 1):  # start from 2
        isPrime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            prime_sum+=i
    return perfect_sum+prime_sum
result=special_sum(30)
print(result)
