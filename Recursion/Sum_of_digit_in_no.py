# Find the sum of digits of a number  
# Eg. sum_digit(1234) OUTPUT: 10

def sum_digit(x):
    if x ==0:
        return 0
    return (x%10)+sum_digit(x//10) # x%10 gives the back values of digit like 4 3 2 1 0
print(sum_digit(1234))

# x//10 gives the divident like 123 12 1 0 
# 1234%10=4  1234//10==123 , sum_digit(123)=123%10=3 123//10=12 and so on 
# 4+3+2+1+0=10