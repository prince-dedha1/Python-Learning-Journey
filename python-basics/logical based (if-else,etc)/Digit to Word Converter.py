# Digit to Word Converter
# Input a number like 123, and print: One Two Three.

num=input("Enter the number: ")
a="1one 2two 3three 4four 5five 6six 7seven 8eight 9nine"
lst=a.split()
for i in range(len(num)):
    for k in lst:
        if k[0]==num[i]:
            print(k[1:],end=" ")
