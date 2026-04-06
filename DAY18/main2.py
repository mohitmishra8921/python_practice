string1 = input("Enter the string:\n")

for ch in string1:
    if string1.count(ch) == 1:
        print("First non-repeating character is:",ch)
        break
else:
    print("No non-repeating character found")

