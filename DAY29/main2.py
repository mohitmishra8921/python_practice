list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]

# Step 1: Length check
if len(list1) != len(list2):
    print("Not Rotated")

else:
    # Step 2: Create combined list
    combined_list = list1 + list1

    # Step 3: Check rotation
    if str(list2) in str(combined_list):
        print("Rotated")
    else:
        print("Not Rotated")