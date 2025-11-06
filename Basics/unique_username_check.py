
# List of existing users
current_users = ["John", "Alice", "Robert", "Emma", "sohel"]

# List of new users trying to register
new_users = ["john", "David", "EMMA", "Riya", "alex"]

# Convert current usernames to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Check each new username
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose another one.")
    else:
        print(f"The username '{new_user}' is available!")
