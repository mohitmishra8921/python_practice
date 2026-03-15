numbers = []
number = int(input("How many numbers you wwant to add in a list ?\n"))
for num in range(number):
    enter_numbers = int(input("Enter the desired numbers : \n"))
    numbers.append(enter_numbers)
print(numbers)    
count_even = 0
count_odd = 0
for num in numbers:
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1
print("Even numbers \n",count_even)       
print("Odd numbers : \n",count_odd)    