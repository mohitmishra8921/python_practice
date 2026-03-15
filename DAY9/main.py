#This program is use to create list of any numbers enter by the user 
while True:
       try:
            num1 = []
            numbers = int(input("How many numbers you want to add in a list ? \n"))
            for num in range(numbers):
                enter_numbers = int(input("Enter desired numbers : \n"))
                num1.append(enter_numbers)
            print("The list of numbers :\n",num1) 
            print("Press ctrl+c  to exit the loop ")
       except Exception as e:     
           print("Invalid input")   
           

