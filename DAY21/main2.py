list1 = [2, 4, 3, 5, 7]
target = 5

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] + list1[j] == target:
         print("The pairs which matches the target: ",(list1[i], list1[j]))

        