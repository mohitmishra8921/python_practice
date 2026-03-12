#CODE TO FIND THE TOTAL SUM OF GIVEN DIGIT
while True:
       try:
        num = int(input("Enter the number: "))
        sum = 0
        while num>0:
            last_digit = num%10
            sum = sum + last_digit
            num = num//10
        print(sum)
       except Exception as e :
           print("invalid literal") 