import csv

file_path_0 = '/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/from_folder/content.csv'
file_path_1 = '/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/from_folder/content.txt'

file_object = open(file_path_1, "r")
data = csv.reader(file_object, delimiter=",")
print('|--------------------------------------------|')
for each in data:
    print(each)
    print("|--------------------------------------------|")
file_object.close()

# file_object = open(file_path, "r")
# data = file_object.readlines()
# file_object.close()
# for each in data:
#     print(each.strip('\n').split(","))

