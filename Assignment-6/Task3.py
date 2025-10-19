mylist=[]
list_size=int(input("Enter the size of your list:"))

for i in range(list_size):
    mylist.append(i)

if list_size>=4:
    newlist=mylist[2:list_size-2]
    print(newlist) 

else:
    print("Not possible")   