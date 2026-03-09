try:
    while True:
        age = int(input("Enter the age : "))
        if (age<13):
            print("User is a child")
        elif(13<=age<18):
            print("User is a teenager")
        else:
            print("User is an adult")    

except Exception as e :
    print("Invalid literal",e)

    