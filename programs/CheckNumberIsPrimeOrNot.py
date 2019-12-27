num = 5
count = 0

if num > 1:
    for i in range(1, num + 1):  # range function >>> The range() function returns a sequence of numbers, starting
        # from 0 by default, and increments by 1 (by default), and ends at a specified number.
        if (num % i) == 0:
            count = count + 1
    if count == 2:
        print(num, "Number is Prime")
    else:
        print(num, "Number is not Prime")
