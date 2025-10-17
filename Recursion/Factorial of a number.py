def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)
# Take input from the user
x = int(input("Enter the No to find the factorial: "))
# Print the result using the factorial function
print(f"The factorial of {x} is = {factorial(x)}")