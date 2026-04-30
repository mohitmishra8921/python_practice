string1 = ("I love programming").split()
largest = ""
for word in string1:
    if len(word)>len(word[0]):
        largest = len(word)
print("Largest word of the sentence:\n",word)