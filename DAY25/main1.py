list1 = [5,2,6,4,3,1]
smallest = list1[0]
second_smallest = list1[0]
for i in list1:
   
    if i <smallest:
         second_smallest=smallest
         smallest= i
       
    elif i>smallest:
       second_smallest=i     
print("Smallest element in the list is:\n",smallest)
print("Second_smallest element in the list is:\n",second_smallest)

