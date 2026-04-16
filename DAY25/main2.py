string1 = input("Enter the string:\n")
#temp = string1
new_string = ""
for ch in string1:
    new_string = ch + new_string
print(new_string)
if new_string!=string1:
    print("not it is not a palindrome")
else:
    print("yes it is  a palindrome")



        


