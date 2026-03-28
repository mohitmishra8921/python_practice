numbers = int(input("How many numbers you want to add in a list ?\n"))
list1 = []

for num in range(numbers):
    enter_numbers = int(input("Enter numbers :\n"))
    list1.append(enter_numbers)
print(list1) 
list2 = []
for num in list1 :
    if num not in list2:
        list2.append(num)  
print(list2)     
 
