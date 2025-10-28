#This will work for only single digit
# mylist=[]

# with open("Sample.txt","r") as f:
#     data=f.read()

#     for i in range(len(data)):
#         if data[i]==",":
#             pass
#         else:
#             if int(data[i])%2==0:
#                 mylist.append(int(data[i]))
#     print(mylist)        

mylist = []

with open("Sample.txt", "r") as f:
    data = f.read()
    data=data.split(",")

    for num in data:
        num = num.strip()  # remove spaces or newlines
        if num.isdigit() and int(num) % 2 == 0:
            mylist.append(int(num))

print(mylist)
print("Total No of Even Numbers:",len(mylist))
