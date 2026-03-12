num = int(input("Enter the number : "))
# last_digit = 0
reverse = 0
while num>0:
    last_digit=  num%10
    reverse = reverse*10+last_digit
    num = num // 10 # there is a simple calculation floor division divide the digit but neglect value after decimal point due to which we get last number of any digit every time in loop 
print("The reverse of given input number by the user :",reverse)    

# The 3-step rule to remember
# Every reverse-number program always does these three steps in a loop:
# Get last digit → % 10
# Add digit to reversed number → reverse * 10 + digit
# Remove last digit from original number → // 10
# If you remember this pattern, you’ll never get stuck on this problem again.
