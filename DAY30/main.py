list1 = [1,2,3,3,4]
list2 = [3,4,5,6]
common_elements =[]
for i in list1:
    if i in list2 and i not in common_elements:
        common_elements.append(i)
print(common_elements)