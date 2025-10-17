# *****
# ****
# ***
# **
# *
rows=int(input("Enter the Number of the rows: "))
for i in range(1,rows+1):
    for j in range(rows+1-i):
        print("*",end="")
    print()
