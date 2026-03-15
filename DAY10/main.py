list1 = []
user_input = int(input("How many numbers you want to add in list1 ? \n"))
for num in range(user_input):
    numbers = int(input("Enter the numbers : \n"))
    list1.append(numbers)
print(list1)    
number_find = int(input("Enter the number you wwant to search :\n"))
print(number_find in list1) 
# if number_find in list1:
#     print("Number found in the list1")
# else:
#     print("Number not found in the list1")    
#Here i use membership operators instead of identity operator there is one advantage of it and one disadvantage ,advantage is i write less line of code and saves memory but disadvantage is readability of the code becomes bad sometime beginners will confuse if they saw or use my code 