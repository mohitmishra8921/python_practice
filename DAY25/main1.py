list1 = [5,2,6,4,3,1]
smallest = float('inf')
second_smallest = float('inf')# here again just like in case of finding largest number so we solve edge case for -ve numbers not it is capable for negative numbers
for i in list1:
   
    if i <smallest:
         second_smallest=smallest
         smallest= i
       
    elif i>smallest and i<second_smallest:
       second_smallest=i     
print("Smallest element in the list is:\n",smallest)
print("Second_smallest element in the list is:\n",second_smallest)

