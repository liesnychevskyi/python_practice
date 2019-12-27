# Approach 1
print("----------------------------------------------------------- 1 th approach")
myList = [1, 2, 3, 4, 6, 25, 33, 45, 55, 55, 45, 9]  # index starts from 0
print(myList)
size = len(myList)  # 12 elements

temp = myList[0]  # first value from the list we put to temp variable
myList[0] = myList[size - 1]  # we put last value from the list on place of first value
myList[size - 1] = temp  # we put first element of the list on place of last element of the list
#  print array after swapping
print(myList)


# Approach 2
print("----------------------------------------------------------- 2 th approach")
myList_2 = [5, 2, 3, 4, 6, 25, 33, 45, 55, 55, 45, 100]  # index starts from 0
print(myList_2)
myList_2[0], myList_2[- 1] = myList_2[- 1], myList_2[0]
print(myList_2)

# Approach 3 using tuple variable
print("----------------------------------------------------------- 3 th approach")
myList_3 = [2, 3, 4, 6, 25, 33, 45, 55, 55, 45]  # index starts from 0
print(myList_3)
get = (myList_3[- 1], myList_3[0])  # we adding first and last variable to tuple variable it is call "Packing"
myList_3[0], myList_3[- 1] = get  # we assign swapped value to get tuple  "Unpacking"
print(myList_3)

# Approach 4 using * operand
print("----------------------------------------------------------- 4 th approach")
myList_4 = [7, 3, 4, 6, 25, 33, 45, 55, 55, 45, 90]  # index starts from 0
print(myList_4)
start, *midle, end = myList_4  # we separate list on 3 different parts

myList_4 = [end, *midle, start]

print(myList_4)

print(start)
print(midle)
print(end)

# Approach 5 using pop
print("----------------------------------------------------------- 5 th approach")
myList_5 = [0, 3, 4, 6, 25, 33, 45, 55, 55, 45, 9]  # index starts from 0
print(myList_5)

first = myList_5.pop(0)
last = myList_5.pop(-1)

myList_5.insert(0, last)
myList_5.append(first)
print(myList_5)
