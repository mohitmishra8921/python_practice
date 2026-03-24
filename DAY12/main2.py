string = input("Enter the word :\n").upper()#important for case error
new_string = ""
for ch in string: 
    new_string = ch + new_string #string concatenation
if new_string == string:
    print("Palindrome")
else:
    print("Not a palindrome")    
print("Reversed: ",new_string)    

  
