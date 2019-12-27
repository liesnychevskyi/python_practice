num = 10

# Approach 1
factorial = 1

if num < 0:
    print("Factorial is not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of ", num, "is", factorial)