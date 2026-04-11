def is_leap(year):
    if year%4!=0 and year%400!=0:
       return False
    elif year%4==0 or year % 400==0 and year%100!=0:
      return True
year = int(input("Enter the random year :\n"))
print(is_leap(year))