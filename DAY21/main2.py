list1 = [2, 4, 3, 5, 7, 9, 1, 6]
target = 10

for i in range(len(list1)):# This outer loops runs in form of row for this list length 
    for j in range(i+1, len(list1)):# this outer loops run in form of columns fro the same length of list
         if list1[i] + list1[j] == target: # This condition is checked using row and column created bu outer loop and inner loop
          print(f"The pairs which matches the target: {(list1[i], list1[j])}")

        