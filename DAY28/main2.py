list1 = [2,4,3,5,7]
target = 7

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]+list1[j] == target:
            print((list1[i],list1[j]),end=",")#efficient for every edge case for finding sum of pairs

            #print((i,j),end=",")this for finding sum but here one edge case left 
          

          
         
          