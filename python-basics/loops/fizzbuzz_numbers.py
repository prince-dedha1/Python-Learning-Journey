# FizzBuzz
# Print numbers from 1 to 50. For multiples of 3, print "Fizz", for 5 print "Buzz", 
# for both, print "FizzBuzz".

for i in range(1,51):
    print(i)
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
