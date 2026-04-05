list1 = []

user_input = int(input("How many numbers you want to add in a list?\n"))

for num in range(user_input):
    enter_numbers = int(input("Enter the numbers:\n"))
    list1.append(enter_numbers)

print("Original list:", list1)
for i in list1:
    if list1[i]<= list1[i+1]:
        print("List is sorted")
    else:
        print("list is not sorted")
        