numbers = []

number = int(input("How many numbers yyou want to add in a list ? \n"))
for num in range(number):
    entered_numbers = int(input("Enter the desired numbers : \n"))
    numbers.append(entered_numbers)
    
print(numbers) 
average = 0
for num in numbers:
    average += (num)/len(numbers)
print(average)    