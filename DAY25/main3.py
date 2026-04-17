string1 = input("Enter the sentence:\n")

count = 0

for i in range(len(string1)):
    if string1[i] != " " and (i == 0 or string1[i-1] == " "):
        count += 1

print("Number of words:", count)