#  Approach 1 clear() method

miList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("My List before cleaning", miList)
miList.clear()
print("My List after cleaning", miList)

#  Approach 2 initialize the lis with no value

miList_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("My List before cleaning", miList_1)
miList_1 = []
print("My List after cleaning", miList_1)

#  Approach 3 *=0 this method removes all the value from the list

miList_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("My List before cleaning", miList_2)
miList_2 *= 0
print("My List after cleaning", miList_2)

#  Approach 3 *=0 this method removes all the value from the list

miList_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("My List before cleaning", miList_3)
del miList_3[0:4]
del miList_3[:]
print("My List after cleaning", miList_3)