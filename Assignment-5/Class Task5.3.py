# def recursive_summation(n):
    
#     if n==0:
#         return 0
#     else:
#         print(n)
#         return n + recursive_summation(n-1)
# # result=recursive_summation(10)    
# # print(result)
# print(recursive_summation(10))
def recursive_summation(n):

    if n>=1:
        print(n)
        return n + recursive_summation(n-1)
# result=recursive_summation(10)    
# print(result)
print(recursive_summation(10))