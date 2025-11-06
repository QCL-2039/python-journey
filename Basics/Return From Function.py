#This is code will illustrate how function return something

def max_num(a,b):
    max=None
    if(a>b):
        max=a
    else:
        max=b
    return max
print("Maximum of these two is:",max_num(10,4))           
