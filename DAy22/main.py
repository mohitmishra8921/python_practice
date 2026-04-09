list1 = [5,4,1,6,2]#when list is not sorted
for i in range(1,5):
    if i not in list1:
        print("The missing value in the list is : ",i)
        break
       
    #this code is correct for each edge case  i tried it in many ways