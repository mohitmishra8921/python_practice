list1 = [1,2,2,3,4,4,5]
unique_list = []
for i in list1:
    if list1.count(i)==1:
        unique_list.append(i)
print(f"The elements whose frequency is one in list1: {unique_list}")
