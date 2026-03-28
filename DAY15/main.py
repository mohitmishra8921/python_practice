name = input("Enter the string:\n")

visited = []

for ch in name:
    if ch not in visited:
        visited.append(ch)
        count = name.count(ch)
        print(ch, ":", count)
        
        

   