list1 = [100,201,30,40,50]
largest = list1[0]

for num in list1:
    if num>largest:
        largest = num
print("largest digit of list1:",largest) 
second_largest = list1[0]
for num in list1:
    if num>second_largest and num!=largest:
        second_largest= num
print("Second largest digit of list1 :",second_largest)        


   