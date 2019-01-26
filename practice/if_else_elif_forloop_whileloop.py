
if 5 > 3:
    print("5 > 2")

num = 0
if num > 0:
    print("This is a positive number")
elif num == 0:
    print("Number is ZERO")
else:
    print("This is a negative number")
# ========================================== FOR loop
num = [1,2,3,4,5,6,7,8,9]
sum = 0
for val in num:
    sum = sum + val
print("Total is ", sum)
# ==========================================
for val in num:
    print(val)
# ------------------------------------------

fruits = ["apple", "orange", "grapes"]
for val in fruits:
    print(val)
else:
    print("No fruits left")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ WHILE loop
print("Enter number : ")

num = int(input())  # casting
sum = 0
i = 1

while i < num:
    sum = sum + i
    i = i + 1
print("Total is :", sum)



