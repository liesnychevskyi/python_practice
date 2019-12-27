arr = [22, 390, 230, 777, 100000000, 21, 7, 3, 500, 60000]

max_value = arr[0]

n = len(arr)  # length of array

for i in range(1, n):  # from 1 to length of array
    if arr[i] > max_value:
        max_value = arr[i]  # swap the max value to grater element

print("Max value in this array is: ", max_value)
#==========================================================================#
min_value = arr[0]

for i in range(1, n):  # from 1 to length of array
    if arr[i] < min_value:
        min_value = arr[i]  # swap the max value to grater element

print("Min value in this array is: ", min_value)