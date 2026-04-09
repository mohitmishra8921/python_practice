list1 = [1,2,4,5]#when list is sorted
n= len(list1)+1
for i in range(1,n+1):
    if i not in  list1:
        print("The missing value in the list is : ",i)
        break
       
    