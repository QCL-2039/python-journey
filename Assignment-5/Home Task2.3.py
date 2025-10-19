def palindromic_triangle(n):

    for i in range(1,n+1):
        for dot in range(n-i):
            print(".",end="")

        for j in range(1,i+1):
           print(j,end="")
            
        for j in range(i-1,0,-1):
           print(j,end="")
        
        for dot in range(n-i):
            print(".",end="")
        print()    
    # for i in range(1,n+1):
    #     print(i,end=" ")
            
    # for j in range(n-1,0,-1):
    #     print(j,end=" ")
palindromic_triangle(6)        
