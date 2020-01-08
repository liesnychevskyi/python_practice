import os

#  "/Users/Stan/PycharmProjects/python_practice/staff_for_identefying"
req_path = input("Enter your directory path: ")
#  req_ext = input("Enter the required files extension .py/ .sh/ .log/ .txt: ")

if os.path.isfile(req_path):
    print(f"The given path ==  {req_path} == is a file. Please pass only directory path")
else:
    all_files = os.listdir(req_path)
    if len(all_files) == 0:
        print(f"The given path >> {req_path} << is empty path - error !!!")
    else:
        req_ext = input("Enter the required files extension .py/ .sh/ .log/ .txt: ")
        req_files = []
        for each_f in all_files:
            if each_f.endswith(req_ext):
                req_files.append(each_f)
        if len(req_files) == 0:
            print(f"There are no <<{req_ext}>> files in the location !!!")
        else:
            print(f"There are {len(req_files)} files in the location of {req_path}")
            print(f"The required files are: {req_files}")
#  ||========================================================================================||
