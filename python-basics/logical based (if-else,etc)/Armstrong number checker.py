# Armstrong Number Checker
# A number is Armstrong if the sum of its digits raised to the power of the number of digits 
# equals the number. Check if the user’s input is an Armstrong number.

num=input("Enter the number: ")
ln=len(num)
num_check=0
for i in num:
    x=int(i)
    num_check = num_check + x**ln
if num_check==int(num):
    print("This number is Armstrong Number: ",num)
else:
    print("This number is not an Armstrong Number..")
