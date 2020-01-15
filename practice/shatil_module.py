import shutil

List = dir(shutil)
for each in List:
    print(each)
# --------------------------------------------------------------|| Copy file
src_file = '/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/dir_0/BIG_BUG.txt'
destination_file = '/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/dir_1/big_bug_1.txt'
# shutil.copyfile(src_file, destination_file)  # It will copy file with different permission access
# shutil.copy(src_file, destination_file)  # It will copy file with same permission access
# shutil.copy2(src_file, destination_file)  # same meta data for destination as well
shutil.copymode()  # just permission not content
shutil.copystat()  #
# --------------------------------------------------------------||
