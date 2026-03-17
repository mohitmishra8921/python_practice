list1 = []
user_input = int(input("How many numbers you want to add in a list ?\n"))
for i in range (user_input):
    enter_number = int(input("Enter numbers :\n"))
    list1.append(enter_number)
print("Original list : ",list1)
unique_list = []
for i in list1:
    if i not in unique_list:
        unique_list.append(i)                             
print("This list contain unique value as compared to original list : ",unique_list)    