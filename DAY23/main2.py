if __name__ == '__main__':#this helps in indention by default according to my logic
 n = int(input("Enter the numbers you want to add in a list:\n"))
list1 = []

for i in input().split():
    list1.append(int(i))

winner = float('-inf')#this is best way to observe largest or second largest in  a list
runner_up = float('-inf')#This logic solve biggest edge case for this queestion pattern for every and each input we can get correct largest and second largest number in a list

for num in list1:
    if num > winner:
        runner_up = winner
        winner = num
    elif num > runner_up and num < winner:
        runner_up = num

print(runner_up)        
                     
                     