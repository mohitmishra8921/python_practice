list1 = [2,4,1,5]
n = len(list1)
for i in range(1,n+1):
    if i not in list1:
        print("The missing value in this list is:",i)
