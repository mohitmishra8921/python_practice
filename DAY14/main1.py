nums = int(input("How many numbers you want to add in a list?\n"))
list1 = []
for num in range(nums):
    numbers = int(input("Enter numbers:\n"))
    list1.append(numbers)
print(list1)    
def max_number(list1):
    max_num = 0
    for num in list1:
        if num>max_num :
            max_num = num
    return max_num
print(f"The maximum number of a list is :\n{max_number(list1)}")        

