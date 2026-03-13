
# while True:
#       try:  
#             print("Simple Calculator \n")
#             num1 = int(input("Enter the first number : "))
#             num2 = int(input("Enter the second number : "))

#             operator = input("Choose the following operators for calculation (*,/,-,+):  ")

#             if(operator == "+"):
#                print(f"The sum of num1 and num2 is : {num1+num2}")
#             elif(operator == "-"):   
#                 print(f"The difference of num1 and num2 is : {num1-num2}") 
#             elif(operator == "/"):
#                 if num2==0:
#                     print("Division by zero is not possible\n")
#                 else:
#                     print(f"The quotient of num1 and num2 is : {num1/num2}") 
#             elif(operator == "*"):
#                 print(f"The product of num1 and num2 is : {num1*num2}") 
#             else:
#                 print("Please enter a valid operator (+ - * /)")  

#       except Exception as e :
#           print("Please enter valid numbers\n")



while True:
      try:  
            print("Simple Calculator \n")
            num1 = int(input("Enter the first number : "))
            num2 = int(input("Enter the second number : "))

            operator = input("Choose the following operators for calculation (*,/,-,+):  ")

            if(operator == "+"):
               print(f"The sum of num1 and num2 is : {num1+num2}")
            elif(operator == "-"):   
                print(f"The difference of num1 and num2 is : {num1-num2}") 
            elif(operator == "/"):
                print(f"The quotient of num1 and num2 is : {num1/num2}") 
            elif(operator == "*"):
                print(f"The product of num1 and num2 is : {num1*num2}") 
            else:
                print("Please enter a valid operator (+ - * /)")  

      except ZeroDivisionError :
          print("Cannot divide by zero\n")          

                   


          

