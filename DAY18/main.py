#This structure is used for creating list by users
range_of_list = int(input("How many numbers you want to add in a list?\n"))
users_list =[]

for num in range(range_of_list):
    enter_numbers = int(input("Enter the numbers : "))
    users_list.append(enter_numbers)
    
print("List created by user input: ",users_list)  

#This whole structure is used for finding largest and second largest number from users list
largest_number = 0 
second_largest = 0
for num in users_list:
    if num>largest_number:
        largest_number=num
    elif num>second_largest and num<largest_number:
        second_largest = num
print("The largest number of user's created list is :",largest_number)        
print("The second largest number of user's created list is :",second_largest)            

      
