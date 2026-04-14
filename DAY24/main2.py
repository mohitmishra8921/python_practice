string1 = "listen"
string2 = "silent"
for ch in string1:
    if  string1.count(ch)!=string2.count(ch):
        print("Not A Anagram")
        break
else:
    print("Anagram")