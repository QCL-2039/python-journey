mylist = [1, 2, 3]
mylist2 = [7, 4, 5]

isCommon = False

for i in range(len(mylist)):
    for j in range(len(mylist2)):
        if mylist[i] == mylist2[j]:
            isCommon = True
            break  # break inner loop
    if isCommon:
        break  # break outer loop if found

print(isCommon)
