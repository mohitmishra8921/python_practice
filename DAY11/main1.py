list_of_numbers = []

user_input = int(input("How many numbers you want to add in a list?\n"))

for num in range(user_input):
    enter_numbers = int(input("Enter the numbers:\n"))
    list_of_numbers.append(enter_numbers)

print("Original list:", list_of_numbers)

new_list = []

for i in range(len(list_of_numbers) - 1, -1, -1):
    new_list.append(list_of_numbers[i])

print("Reversed list:", new_list)