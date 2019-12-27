myList = ["geeks", "billion", "geeks"]
print(myList)
searchable_word = "geeks"
times_appearance = 2
count = 0

for i in range(0, len(myList)):
    if myList[i] == searchable_word:
        count = count + 1
        if count == 2:
            del myList[i]
            print(myList)




