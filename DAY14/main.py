numbers = int(input("How many numbers you want to add in a list ?\n"))
list1 = []

for num in range(numbers):
    enter_numbers = int(input("Enter numbers :\n"))
    list1.append(enter_numbers)
print(list1)    
def sum_of_numbers(list1):
    total_sum = 0
    for num in list1:
        total_sum += num
    return total_sum
print(f"The total sum of numbers in a list is :\n{sum_of_numbers(list1)}")
