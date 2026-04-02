string1 = input("Enter the first word : ").lower()
string2 = input("Enter the second word :").lower()
print(sorted(string1))
print(sorted(string2))
if  sorted(string1)==sorted(string2):
    print("Yes it is Anagram")
else:
    print("Not it is not")

# 💡 Correct Thinking (IMPORTANT 🔥)

# 👉 Anagram hone ke liye:

# Length same honi chahiye
# Characters same hone chahiye
# Frequency same honi chahiye    