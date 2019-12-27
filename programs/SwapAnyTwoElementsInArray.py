myList = [33, 7, 3, 1000000]
print(myList)

# Approach 1 Simple swap
pos1, pos2 = 1, 3
myList[pos1], myList[pos2] = myList[pos2], myList[pos1]
print(myList)

# Approach 2 Using inbuilt.pop() function
myList_1 = [33, 7, 3, 1000000]
print(myList_1)

pos1, pos2 = 1, 3
first_value = myList_1.pop(pos1)      # 7
second_value = myList_1.pop(pos2-1)   # 1000000

print(first_value)
print(second_value)

myList_1.insert(pos1, second_value)
myList_1.insert(pos2, first_value)
print(myList_1)

#  Approach 3 using tuple
myList_2 = [33, 0, 3, 1]
print(myList_2)
pos1, pos2 = 1, 3
get = (myList_2[pos1], myList_2[pos2])
print(type(get))
myList_2[pos2], myList_2[pos1] = get
print(myList_2)


