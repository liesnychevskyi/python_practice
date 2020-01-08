import os

path = "/Users/Stan/PycharmProjects/python_practice/staff_for_identifying"
# print(list(os.walk(path)))
# print("|----------------------------------------------------------------------------------|")
# for each in list(os.walk(path)):
#     print(each, "\n")

# for root, directory, file in os.walk(path):
#     print(root)
#     print(directory)
#     print(file)
#     print("\n")
print("\n")
for root, directory, file in os.walk(path, topdown=True):
    if len(file) != 0:
        print(root, directory, file)
        print("\n")
        for each in file:
            print("PATH OF FILE: ==>>    ", os.path.join(root, each))
            print("|-------------------------------------------------------------------------------------")