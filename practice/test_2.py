# variables is case-sensitive
# letters (a-z), underscore, numbers(0-9)
# - comment
# Ctrl + /  - comment short cut
print("Hello World!!!")
x = 5
y = "Automation"
print(x)
print(y)

print("Hello " + y)

x = 10
y = 30
print(x + y)

if 10 > 5:
   print("10 is grated than 5")

def sum(a,b):
    print(a + b)

x = sum(20, 30)

x = 5
y = 2.5
z = 4j
print(type(x))
print(type(y))
print(type(z))
print(z)

# Casting

x = int(2)  # 2
y = int(2.5)  # 2
z = float(1)  # 1.0
p = str(10)  # "10"

print(x)
print(z)
print(y)
print(p)

x = "Hello World !"
print(x[1])  # printing index
print(x[6:11])  # printing from to till
print(x.lower())
print(x.upper())
print(x.strip())
print(x.replace("e", "A"))
x = "Hello,World.."
print(x.split(","))

print("Enter your name : ") # input function
x = input()
print("Hello, " + x)
