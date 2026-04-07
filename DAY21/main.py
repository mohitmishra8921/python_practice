list1 = [5,10,15,20]
largest = 0
second_largest = 0
for i in list1:
       if i>largest:
            second_largest=largest
            largest=i
       elif i < largest and i > second_largest:
          second_largest=i
print("Largest digit of list:",largest)
print("Second largest digit of list:",second_largest)        