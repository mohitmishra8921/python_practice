#CODE TO FIND THE TOTAL SUM OF GIVEN DIGIT
while True:
       try:
        num = int(input("Enter the number: "))
        sum = 0
        while num>0:
            last_digit = num%10
            sum = sum + last_digit
            num = num//10
        print("The sum of given digit by the user : ",sum)
       except Exception as e :
           print("invalid literal") 

# Thinking Steps
# Ask yourself:
# 1️⃣ How can you get the last digit of a number?
# 2️⃣ How will you add that digit to a sum variable?
# 3️⃣ After taking the last digit, how will you remove it from the number?
# 4️⃣ When should the loop stop?
