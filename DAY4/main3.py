#exact problem for day 
while True:
 num = int(input("Enter the number : "))
 for i in range (1,11):
    print(num,"*",i,"=",num *i)



#Another way to show previous problem
 while True:
  num = int(input("Enter the number : "))
  for i in range (1,11):
    print(f"{num} * {i} = {num*i}")