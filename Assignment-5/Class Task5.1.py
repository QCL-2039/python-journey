# def one_to_N(n):
#     if n == 0:
#         return
#     one_to_N(n - 1)
#     print(n,end=" ")

# num=int(input("Enter your number:"))
# one_to_N(num)

def one_to_N(n):
    if n>0:
        one_to_N(n - 1)
        print(n,end=" ")

num=int(input("Enter your number:"))
one_to_N(num)

