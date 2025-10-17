def chk_palindrome(x):
    if x<10:
        return str(x)
    return str(x%10)+(chk_palindrome(x//10))
num=5555
rev=chk_palindrome(num)
if num==rev:
    print(" Palindrome ")
else:
    print(" Not a Palindrome ")