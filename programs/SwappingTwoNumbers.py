# num_1 = 10
# num_2 = 20

# Approach1
num_1 = input("Enter num_1 value :")
num_2 = input("Enter num_2 value :")

print("Value before swapping: ", num_1)
print("Value before swapping: ", num_2)

# temp = num_1   # 10
# num_1 = num_2  # 20
# num_2 = temp   # 10

print("Value after num_1 swapping: ", num_1)
print("Value after num_2 swapping: ", num_2)
# Approach2
num_1, num_2 = num_2, num_1

print("Value after num_1 swapping: ", num_1)
print("Value after num_2 swapping: ", num_2)
