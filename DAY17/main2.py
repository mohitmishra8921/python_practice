#Use This Code For Finding User Input Reverse
# number = int(input("Enter the number you want to get reverse of it: \n"))
# reverse = 0
# for i in range(number):
#     lastdigit = number%10
#     if lastdigit<1:
#         break
#     reverse = reverse*10 + lastdigit
#     number= number//10
# print(f"Reverse of user input:{reverse}\n")

# Use This Code For Finding User Input Number Sum
# number = int(input("Enter the number you want to get sum of it: \n"))
# sum_of_numbers = 0
# for i in range(number):
#     lastdigit = number%10
#     if lastdigit<1:
#         break
#     sum_of_numbers= sum_of_numbers + lastdigit
#     number= number//10
# print(f"Sum of user input:{sum_of_numbers}\n")

# Use This Code For Finding total numbers in User Input Number 
number = int(input("Enter the number you want : \n"))# important thing need to be noticed here loop doesn't work on integer so for counting total numbers we have two ways one to typecaste the range or didn;t typecast user input
count = 0
for num in str(number):
    count = count+1
print(f"Total numbers :{count}")



    
    