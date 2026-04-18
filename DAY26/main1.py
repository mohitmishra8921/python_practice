list1 = [1,2,2,3,1,4]
unique_list = []
for i in list1:
    if i not in unique_list:
        unique_list.append(i)
print(f"Unique list:\n{unique_list}")