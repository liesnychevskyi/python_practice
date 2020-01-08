from_file = "/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/from_folder/content.txt"
to_file = "/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/to_folder/content_copy.txt"

source_file_object = open(from_file, "r")
content = source_file_object.read()
source_file_object.close()
print(content)

copy_to = open(to_file, "w")
copy_to.write(content)
copy_to.close()


