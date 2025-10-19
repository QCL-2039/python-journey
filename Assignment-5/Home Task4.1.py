def reverse_digit(n):
    if n==0:
        return 0
    else:
        print(n%10)
        reverse_digit(n//10)
N=int(input("Enter your Number:"))        
reverse_digit(N)        
