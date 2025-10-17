def rev_n_no(n):
    if n==0:
        return 
    print (n , end=" ")
    rev_n_no(n-1)
a=10
rev_n_no(a)