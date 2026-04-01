list1 = [1,2,3,4,5]
list2 = [1,2,9,8,7]

list3 = []

for i in list1:
    if i in list2 and i not in list3:
        list3.append(i)

print("Common elements of list1 and list2:\n", list3)