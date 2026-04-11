n = int(input())
list1 =[] 
winner = 0
runner_up =0
for n in input().split():#This is another way through which we can create list by input from user by prevent memory usage
    list1.append(int(n))
for n in list1: # It just like to find largest and second largest number in a list 
    if n>winner:
        runner_up = winner
        winner = n
    elif n>runner_up and n<winner:
        runner_up = n 
print(runner_up)        
                     