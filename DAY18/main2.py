string = input("Enter the string:\n")

for ch in string:
    if string.count(ch) == 1:
        print("First non-repeating character is:", ch)
        break
else:
    print("No non-repeating character found")

