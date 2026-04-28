list1 = [1,2,3,4]
list2 = [3,4,1,2]
list3 = list1 + list1
for i in list2:
    if list2  in list3:
        print("No it's not the rotated version of list1")
        break
else:
    print("Yes list2 is rotated of list1")

        