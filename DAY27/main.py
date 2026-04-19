number = int(input("Enter the number you want check is either armstrong or not:\n"))
n= len(str(number))
original_num= number
sum_number = 0
for num in str(number):
    sum_number+= int(num)**n
print("Matched to original number:",sum_number)
if sum_number!=original_num:
    print("NOT A ARMSTRONG")
else:
    print("ARMSTRONG")
