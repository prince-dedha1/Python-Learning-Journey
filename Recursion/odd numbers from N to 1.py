def rev_odd(n):
    if n==0:  # Base Case
        return 
    if n%2 != 0 :
        print(n , end=" ")
    rev_odd(n-1)
rev_odd(5)