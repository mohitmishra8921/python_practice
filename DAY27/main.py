number = int(input("Enter the number: "))

n = len(str(number))        # number of digits
original_num = number
sum_number = 0

# calculate sum of digits^n
for digit in str(number):
    sum_number += int(digit) ** n

# final comparison (IMPORTANT: loop ke baad)
if sum_number == original_num:
    print("ARMSTRONG")
else:
    print("NOT AN ARMSTRONG")