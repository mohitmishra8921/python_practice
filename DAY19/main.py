list1 = []

user_input = int(input("How many numbers you want to add in a list?\n"))

for _ in range(user_input):
    num = int(input("Enter the numbers:\n"))
    list1.append(num)

print("Original list:", list1)

is_sorted = True
prev = list1[0]

for current in list1[1:]:
    if current < prev:
        is_sorted = False
        break
    prev = current

if is_sorted:
    print("List is sorted")
else:
    print("List is not sorted")