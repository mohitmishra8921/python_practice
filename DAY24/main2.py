string1 = "liisten"
string2 = "silent"
for ch in string1:
    if  string1.count(ch)==string2.count(ch):
        print("Anagram")
        break
else:
    print("Not A Anagram")