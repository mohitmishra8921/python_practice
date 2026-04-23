# string1 = input("Enter the string: \n").split()



# new_string1 = ""
# reverse_string1 = " "

# for ch1 in string1:
#     if ch1 ==string1[0]:
#         new_string1 = (f'{ch1 + new_string1}')
#     else:
#         new_string1 = ch1 + new_string1
#         for ch in new_string1:
#             reverse_string1 = ch + reverse_string1  
# print(reverse_string1) 
# Another way of this problem
string1 = input("Enter the string:\n").split()

result = []

for word in string1:
    result.append(word[::-1])

final = " ".join(result)

print(final)            
               



