#problem 2 of day 12
while True:
    string = input("Enter the valid string : \n")
    new_string =  ""
    for ch in string:
        new_string = ch + new_string
    print(new_string)


