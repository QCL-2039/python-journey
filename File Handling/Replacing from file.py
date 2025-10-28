# This will replace the word "Java" with "Python" in the file

# Open the file in read and write mode ("r+")
with open("Test.txt", "r+") as f:
    # Read the current content
    data = f.read()
    print("Before replacement:")
    print(data)

    # Replace all occurrences of "Java" with "Python"
    data = data.replace("Java", "Python")

    # Move the pointer to the beginning before writing
    f.seek(0)

    # Write the updated content back to the file
    f.write(data)