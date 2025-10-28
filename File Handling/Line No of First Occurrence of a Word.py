word = input("Enter your word: ")

with open("Test.txt", "r") as f:
    line = 0
    data = f.read()

    # Count total number of lines
    for i in range(len(data)):
        if data[i] == "\n":
            line += 1
    line += 1  # add 1 for the last line (no '\n' at the end)

    f.seek(0)

    # Search word line by line
    for i in range(1, line + 1):
        check_line_no = f.readline()
        if check_line_no.find(word) != -1:   
            print(word, "found in line:", i)
            break
    else:
        print(word, "not found in any line.")
# word = input("Enter your word: ")

# with open("Test.txt", "r") as f:
#     line_no = 0
#     found = False

#     for line in f:
#         line_no += 1
#         if line.find(word) != -1:   # check properly
#             print(word, "found in line:", line_no)
#             found = True
#             break

#     if not found:
#         print(word, "not found in any line.")
