#exact problem for day 
try:
   while True:
     num = int(input("Enter the number : "))
     for i in range (1,11):
      print(num,"X",i,"=",num *i)
except Exception as e:
 print("Invalid input",e)

# Another way to show previous problem
try:
   while True:
     num = int(input("Enter the number : "))
     for i in range (1,11):
      print(f"{num} * {i} = {num*i}")

except Exception as e :
  print("Invalid input",e)      