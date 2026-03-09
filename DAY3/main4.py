try:
 while True:
  num = int(input("Enter the number : "))

  if (num%2==0):
    print("even number")

  else:
    print("odd number")   
except Exception as e:
  print("invalid literal",e)     