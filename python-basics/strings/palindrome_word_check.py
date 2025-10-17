# Check if a String is a Palindrome
str1=input("Enter the string: ")
str2=""
if str1.isalpha():
    for i in range(-len(str1),0):
        str2 = str2+str1[i]
else:
    print("Not valid string ")
if str2==str1:
    print(str1,"  is a palindrome word..")
else:
    print(str1,"  is not a palindrome word..")