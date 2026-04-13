string1 = "liissten"
string2 = "sisilent"
for ch in string1:
    if  string1.count(ch)!=string2.count(ch):
        print("Not A Anagram")
        break
else:
    print("Anagram")