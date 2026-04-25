list1 = [1,2,2,2,2,3,3,3,4]

max_count = 0

for i in list1:
    if list1.count(i)>max_count:
        max_count = list1.count(i)
        ans=i
print(ans)

