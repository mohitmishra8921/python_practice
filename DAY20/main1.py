string1 = input("Enter the string you want: ").lower()#lower function is used here to maintain edge case of code
vowels = ("a","e","i","o","u")
count_vowels=0
count_consonents=0

for ch in string1:
    if ch.isalpha():#this edge case is real word issue bcz we need to check only letters in string sometime user provide number with it
        if ch in vowels:
          count_vowels+=1
        else:
           print("Neither vowels nor consonents")   

print("Number of vowels in given string:\n",count_vowels)  
print("Number of consonents in given string:\n",count_consonents)   