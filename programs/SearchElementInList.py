#  Approach 1
myList = [1, 2, 3, 5, 7, 30, 70]
ele = 700
flag = 0

for i in myList:
    if i == ele:
        print("Element found")
        flag = 1
        break
if flag == 0:
    print("Element not found")

#  Approach 2 using IN operator

myList_1 = [1, 2, 3, 5, 7, 30, 70]
ele = 7
if ele in myList_1:
    print("Element found in List 'myList_1'")
else:
    print("Element not found in List 'myList_1'")



