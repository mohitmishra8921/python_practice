list1 = [1,1,0,1,1,1]

current_count = 0
max_count = 0

for i in list1:
    if i == 1:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print("Maximum consecutive 1's:", max_count)