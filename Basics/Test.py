# mylist=list(range(1,10,2))
# print(mylist)

# squares_num=[i**2 for i in range(1,11)]
# print(squares_num)

# l_limit=int(input("Enter the lower limit:"))
# u_limit=int(input("Enter the upper limit:"))

# num=[i for i in range(l_limit,u_limit)]
# print(num)
# l=[1,2,3]
# r=l
# r.append(5)
# print(l)
# r=l.copy()
# print(r)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    if message != 'quit':
       print(message)