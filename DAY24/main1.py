list1 = [1,2,3,2,4,5,1]
Duplicates = []
for i in list1:
    if i not in Duplicates and list1.count(i)>=2:
        Duplicates.append(i)
print(f"Duplicates element in list1: {Duplicates}")

    