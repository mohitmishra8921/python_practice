list1 = [6,4,5,2,1]
n= len(list1)+1
for i in range(1,n+1):
    if i not in  list1:
        print("The missing value in the list is : ",i)
        break
       
    