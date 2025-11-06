person={
    'name':"Sohel Rana",
    'age':24,
    'id':573
}
print(person['age'])

user = {
    'user_name': ['Sohel', 'Rana', 'Meher'],
    'user_pass': [1, 2, 3]
}

# Print each username with its matching password
for i in range(len(user['user_name'])):
    name = user['user_name'][i]
    password = user['user_pass'][i]
    print(f"Username: {name}, Password: {password}")

university={
    'uni_name':['DU','NSU','BUET'],
    'rank':[1,2,3]
}
for i in range(len(university['uni_name'])):
    uname=university['uni_name'][i]
    rank=university['rank'][i]
    print(f"{uname} rankd: {rank}")

user = {
    'user_name': [],
    'user_pass': []
}

for i in range(3):
    name = input("Enter your name: ")
    user['user_name'].append(name)  
    password = input("Enter your password: ")
    user['user_pass'].append(password) 

# Display all users
for i in range(len(user['user_name'])):
    name = user['user_name'][i]
    password = user['user_pass'][i]
    print(f"Username: {name}, Password: {password}")
