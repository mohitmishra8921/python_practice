count_odd = 0
count_even = 0
for i in range(10): # The range defines the thing under the loop will run accordding to range number of times
       num = int(input("number :"))
       if i%2==0:
            count_even+=1
       else:
           count_odd+=1
print("Even numbers :",count_even) 
print("Odd numbers :",count_odd)       
      