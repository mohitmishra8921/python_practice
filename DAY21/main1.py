string1 = input('Enter the valid string : ').lower().strip()
alphabets = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
for ch in alphabets:
   if ch not in string1:
        print("not a pangram")
        break
else:
    print("pangram")
        
    
        