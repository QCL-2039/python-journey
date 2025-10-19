def show_palindrome(n):
    for i in range(1,n+1):
        print(i,end="")
    for j in range(n-1,0,-1):
        print(j,end="")   
N=int(input("Enter your number:"))        
show_palindrome(N)        