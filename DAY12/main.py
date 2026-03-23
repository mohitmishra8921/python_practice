
while True:
       
     words = input("Enter the word : \n")
     vowel = ("a","e","i","o","u","A","E","I","O","U")
     count_vowel = 0
     for ch in words:
         if ch in vowel:
            count_vowel+=1
     print(count_vowel)  
        


   