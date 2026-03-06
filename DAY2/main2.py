#2. LOGIC BUILDER QUESTION FOR TODAY
count = 0
i = 0
while (i<50):
    i+=1 
    if i %4==0 and i%8 !=0:
        count +=1
        print(i)   
print(count)    

# 3. MEDIUM LEVEL QUESTION FOR TODAY¶
total_sum = 0
for i in range (1,30):
     temp = i
     if i % 2!= 0:
         
       while temp>0:
          digit = temp*temp
          total_sum += digit
print(total_sum)

sum_by_3 = 0
for i in range (1,30):
     if i % 2!= 0:
         sum_by_3 += i*i
print(sum_by_3)     


total = 0
for i in range (1,20):
    if i%2==0:
        total +=i*i
print(total)        
        

 # 4. HARD PROBLEM OF DAY 2ND
largest = 0

for i in range(1, 101):
    if i % 7 == 0:
        largest = i

print("Largest number divisible by 7:", largest)
