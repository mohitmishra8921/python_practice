#Programs to count even numbers between specific range

count = 0
for i in range (1,100):
    if i %2 == 0:
        count +=1
print("Even numbers between 1 to 100:",count)        