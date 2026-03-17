num = []
user_demand = int(input("How many numbers you wwant to add in a list ?\n"))
for i in range(user_demand):
    enter_number = int(input("Enter numbers : \n"))
    num.append(enter_number)
print("The list created by user : \n",num)
largest = 0
second_largest =0
for i in num:
    if i>largest:
        largest = i 
for i in num:
    if i>second_largest and i<largest:
            second_largest = i
print("Largest number of user's liist :\n",largest)
print("Second largest number of user's list :\n",second_largest)  

