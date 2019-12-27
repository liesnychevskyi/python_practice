def factorial(n):
    # if n == 0 or n == 1:
    #     return 1
    # else:
    #     return n * factorial(n - 1)
    # Ternary operator
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


num = 5

print("Factorial of", num, "is", factorial(num))
