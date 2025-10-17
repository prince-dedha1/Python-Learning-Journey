# Leap Year Checker
# Ask for a year and check if it’s a leap year.

year=int(input("Enter the current year : "))
if year % 4==0:
    print(year," is a leap year...")
elif year % 100 == 0 and year % 400 == 0:
    print(year," is a leap year...")
else:
    print(year," is not a leap year...")