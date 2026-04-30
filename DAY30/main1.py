string1 = ("I love programming").split()
largest = ""
for word in string1:
    if len(word) > len(largest):
        largest = word
print("Largest word of the sentence:\n",largest)
        
   
    