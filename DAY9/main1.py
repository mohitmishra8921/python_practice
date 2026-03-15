#It just a modified version of previous code one simple change is here i add one thing that count smallest number of user list
numbers = []

number = int(input("How many numbers yyou want to add in a list ? \n"))
for num in range(number):
    entered_numbers = int(input("Enter the desired numbers : \n"))
    numbers.append(entered_numbers)
    
print(numbers) 
smallest = numbers[0]
for num in numbers:
    if num<smallest:
        smallest = num
print("The smallest number of user list : ",smallest)           
