def sum_firstN(n):
    if n==0: # base case 
        return 0
    return n+sum_firstN(n-1)  # 10+9+8+7+sum_firstN(6....)
print(sum_firstN(10))