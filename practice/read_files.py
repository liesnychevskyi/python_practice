# import os
# import sys
# path = input("Enter your directory path: ")
# path_folder = "/Users/Stan/PycharmProjects/python_practice/staff_for_identefying"
#
# if os.path.exists(path):
#     df_l = os.listdir(path_folder)
# else:
#     print("Please enter valid path >>>")
#     sys.exit()
#
# p1 = os.path.join(path, df_l[0])
# p2 = os.path.join(path, df_l[1])
# p3 = os.path.join(path, df_l[2])
#
# print(p1)
# print(p2)
# print(p3)
# print("|---------------------------------------------------------------------|")
#
#
# if os.path.isfile(p2):
#     print(f"{p2} It is a file")
# else:
#     print(f"{p2} -------- it is a directory")
#
# if os.path.isfile(p1):
#     print(f"{p1} -------- It is a file")
# else:
#     print(f"{p1} it is a directory")

# ------------------------------------------------------------------------//

import os
import sys

path = input("Enter your directory path: ")
path_folder = "/Users/Stan/PycharmProjects/python_practice/staff_for_identefying"

if os.path.exists(path):
    df_l = os.listdir(path_folder)
else:
    print("Please enter valid path >>>")
    sys.exit()

list_of_files_dir = os.listdir(path)
print(list_of_files_dir)
count = 1

for each_element in list_of_files_dir:
    f_d_p = os.path.join(path, each_element)
    print(f"Element is: --- {count} {each_element} path is: {f_d_p}")
    count = + count + 1
    print('|-----------------------------------------------------------------------------------------------------|')

    if os.path.isfile(f_d_p):
        print(f'{f_d_p} is a file !!!')
    else:
        print(f'{f_d_p} is a directory!!!')
        print('|-----------------------------------------------------------------------------------------------------|')
