def n_no(n):
    if n==0:
        return 
    n_no(n-1)
    print (n , end=" ")
a=10
n_no(a)