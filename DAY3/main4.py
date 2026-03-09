try:
 while True:
  num = int(input("Enter the number : "))

  if (num%2==0):
    print("even number")

  elif (num%2!=0):
    print("odd number ")

  else:
    print("other number")   
except Exception as e:
  print("invalid literal",e)     