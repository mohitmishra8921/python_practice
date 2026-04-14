list1 = [1,2,3]
list2 = [1,2,3,4,5]
for i in list1:
    if i not in list2:
        print("NO list1 is not a subset of list2")
        break
else:
    print("Yes list1 is a subset of list2")
