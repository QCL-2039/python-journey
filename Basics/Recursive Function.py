#This is code illustrate the recursive function

def Show(n):
    if n>0:
        print(n)#5,4,3,2,1
        Show(n-1)
        print("Tracing Back:")
        print(n)#1,2,3,4,5
Show(5)        
