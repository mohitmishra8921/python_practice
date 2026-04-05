list1 = [2,0,8,4,0]
list_of_zeroes = []
for i in list1:
    if i not in list_of_zeroes and i !=0:
        list_of_zeroes.append(i)
for i in list1:
    if i==0:
        list_of_zeroes.append(i)
print(list_of_zeroes)        