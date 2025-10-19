mylist=[]
list_size=int(input("Enter the size of your list:"))

for i in range(list_size):
    mylist.append(i)
    
new_list=[]
for j in range(list_size-1,-1,-1):
    new_list.append(mylist[j])

print(mylist)