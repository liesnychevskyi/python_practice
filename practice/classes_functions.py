import os
import time
import platform


# if platform.system() == "Windows":
#     print("Please wait. Cleaning the screen...")
#     time.sleep(2)  # waiting 2 seconds
#     os.system("cls")  # cleaning command line for windows platform
#     print("Please wait finding list of the files...")
#     time.sleep(2)
#     os.system("dir")  # printing files from the folder
# else:
#     print("Please wait. Cleaning the screen...")
#     time.sleep(2)  # waiting 2 seconds
#     os.system("clear")  # cleaning command line for linux platform
#     print("Please wait finding list of the files...")
#     time.sleep(2)
#     os.system("ls -lrt")  # printing files from the folder linux
######################################################

def my_code(cmd1, cmd2):
    print("Please wait. Cleaning the screen...")
    time.sleep(2)  # waiting 2 seconds
    os.system(cmd1)  # cleaning command line for windows platform
    print("Please wait finding list of the files...")
    time.sleep(2)
    os.system(cmd2)  # printing files from the folder


if platform.system() == "Windows":
    my_code("cls", "dir")
else:
    my_code("clear", "ls -lrt")
