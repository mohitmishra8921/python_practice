while True:
       try:
          number = int(input("Guess the secret number :\n"))
          secret_number = 15
          if(number == secret_number):
            print("Yeah you guess right ✅ \n")
            break
          else:
              print("Wrong guess ❌\n")      
              print("Try again\n")
       except Exception as e :
           print("Enter only numbers\n")
                  
        
 
