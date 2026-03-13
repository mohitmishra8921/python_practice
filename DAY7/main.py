while True:
      try:
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
                print("Plzz enter valid operator and operand")       
      except Exception as e :
          print(e)
                   


          

