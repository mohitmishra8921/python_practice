string1 = input("Enter the string you want:\n")
for ch in string1:
    if string1.count(ch)==1:
        print(f"First non repeating character is: {ch}")
        break