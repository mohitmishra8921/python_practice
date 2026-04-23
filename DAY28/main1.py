string1 = input("Enter the string:\n").split()

new_string = []
for ch in string1:
    new_string.append(ch)
print(new_string)

new_string1 = ""
reverse_string1 = ""

for ch1 in new_string:
    if ch1 ==new_string[0]:
         new_string1 = ch1 + new_string1
    else:
         new_string1 = ch1 + new_string1
         
         for ch in new_string1:
             reverse_string1 = ch + reverse_string1
             

print(reverse_string1)             
             


