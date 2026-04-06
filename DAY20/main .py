user_input = int(input("How many numbers you want to add in a list ? "))
new_list = []

for i in range(user_input):
    enter_numbers = int(input("Enter the numbers: "))
    new_list.append(enter_numbers)
print(new_list)    
unique_list = []
for i in new_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)    