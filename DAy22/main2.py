list1 = [10,20,30,40,50]
rotate_list = []
for i in list1[-2:]:# Remeber one thing when work with lists than use index as their range 
    if i>3:
        rotate_list.append(i)
for i in list1[:3]:
            rotate_list.append(i)
print(f"Rotated list: {rotate_list}")
