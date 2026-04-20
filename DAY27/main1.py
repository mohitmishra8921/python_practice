list1 = [1,2,3,2,4,1]
seen =[]
for i in list1:
    if i not in seen:
        seen.append(i)
    elif i in seen:
        print(f"First repeating number is:{i}")
        break

    
