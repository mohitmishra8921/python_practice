list1 = [4,3,1,5,5]#Here we use sorted to ignore orders
list2 = [1,5,4,3]
a = sorted(list1)
b = sorted(list2)
print(a) 
print(b) 
if a == b:
    print("Both lists are equal")
else:
    print("Both lists are not equal")    