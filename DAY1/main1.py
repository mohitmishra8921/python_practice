# hard problems for today
total_sum = 0

for i in range(1, 51):   # 1 to 50
    temp = i             # copy number
    while temp > 0:
        digit = temp % 10
        total_sum += digit
        temp = temp // 10

print("Final Sum:", total_sum)

total_sum = 0

for i in range (1 ,100):
    temp = i
    while temp>0:
        digit = temp %10
        total_sum += digit
        temp = temp//10
        
print("FINAL SUM :",total_sum)    

total_sum = 0
for i in range (1 ,101):
    temp = i
    if i % 2==0:
        
      while temp>0:
          digit = temp % 10
          total_sum += digit
          temp = temp // 10
print("SUM OF EVEN NUMBERS:",total_sum)          