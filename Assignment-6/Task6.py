list1=[1,2,3,4,5]
list2=[1,2,3]
even_list = []

for num in list1 + list2:  
    if num % 2 == 0:
        even_list.append(num)
print(even_list)


# list1=[1,2,3,4,5]
# list2=[1,2,3]
# new_list=list1+list2

# for i in range(len(new_list)):
#     if new_list[i]%2==0:
#         new_list.append(new_list[i])
# print(new_list)        