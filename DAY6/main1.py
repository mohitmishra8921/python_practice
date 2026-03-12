while True:
     try:
         num = int(input("Enter the number : "))
         temp = num
         reverse = 0
         while num>0:
           last_digit = num%10
           reverse = reverse * 10 + last_digit
           num = num//10
         
         print(reverse)  
         if(reverse == temp):
            print("The given number is palindrome: ",temp)
         else:
            print("No the number is not a palindrome :",temp)  
     except Exception as e :
        print("invalid literal")


# 🧠 Important Lesson You Just Learned
# Whenever we modify a variable inside a loop, we should store the original value.
# Example problems where this happens:
# Palindrome number
# Armstrong number
# Reverse number
# Sum of digits
# This pattern will appear many times in programming.

    
       
    

    