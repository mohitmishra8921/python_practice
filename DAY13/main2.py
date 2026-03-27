num1 = int(input("Enter the first number : \n"))
num2 = int(input("Enter the second number : \n"))
num3 = int(input("Enter the third number : \n"))
def find_max(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    
print("The maximum number is: ")    
print(find_max(num1,num2,num3))    

