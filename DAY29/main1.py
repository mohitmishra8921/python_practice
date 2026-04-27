string1 =("i love python").split()
result = []
for words in string1:
    result = words[0].upper()+ words[1:]
    print(result,"",end="")

