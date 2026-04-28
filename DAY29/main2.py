list1 = [1,2,3,4]
list2 = [3,4,1,2]

if len(list1)!=len(list2):
   print("Not Rotated")
else:
    new_list = list1+list1
    if str(list2) in str(new_list):
       print("Rotated")
    else:
       print("Not Rotated")
        
   


    