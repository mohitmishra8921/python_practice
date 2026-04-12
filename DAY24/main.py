# Print an array of the elements that do not sum to .
x = int(input("Enter first value: "))
y = int(input("Enter second value: "))
z = int(input("Enter third value: "))
n = int(input("Enter fourth value: "))

result = [[i, j, k] 
          for i in range(x+1) 
          for j in range(y+1) 
          for k in range(z+1) 
          if i + j + k != n]

print(result)