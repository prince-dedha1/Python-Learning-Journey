def count_digit(x):
    if x==0:
        return 0
    return 1+ count_digit(x//10)   # 1+(1+count_digit(12345678)).....
print(count_digit(123456789))