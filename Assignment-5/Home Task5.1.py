def sequence_recursive(n):
    if n==0:
        return 0
    else:
        print(n)
        return n+ pow(-1,n+1)*sequence_recursive(n-1)
    
N=int(input("Enter your N:"))    
print(sequence_recursive(N))