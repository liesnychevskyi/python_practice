def calculator():
    # first = int(input("Enter first number: "))
    # second = int(input("Enter second number: "))

    first = eval(input("Enter first number: "))  # if you want to add string, enter it like this: "Some string"
    second = eval(input("Enter second number: "))
    res = first + second
    return res


r = calculator()
print(r)
