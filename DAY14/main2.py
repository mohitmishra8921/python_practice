nums = int(input("How many numbers you want to add in a list?\n"))
list1 = []
for num in range(nums):
    numbers = int(input("Enter numbers:\n"))
    list1.append(numbers)
print(list1)    
def max_number(list1):
    count_even = 0
    count_odd = 0
    for num in list1:
        if (num%2==0):
            count_even += 1
        else:
            count_odd += 1        
    return count_even,count_odd
    

print(f"The number of even and odd number in a  list is :\n{max_number(list1)}")        

