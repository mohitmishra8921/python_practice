while True:
     try:
    
       num1 = int(input("Enter the first number : "))
       num2 = int (input("Enter the second number : "))
       num3 = int (input("Enter the third number : "))
       print("The numbers enter by user : \n",num1,num2,num3) 

       if(num1>=num2 and num1>=num3 ):# i use equals condition bcz some time two numbers among of three numbers must become equal 
           print("largest number is num1 : \n",num1)
       elif(num2>=num1 and num2>=num3):
           print("largest number is num2 : \n",num2)
       elif(num3>=num2 and num3>=num1):
           print("largest number is num3 : \n",num3)  
    
    
     except Exception as e:
      print("Invalid literal")    