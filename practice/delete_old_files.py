import os
import sys
import datetime

req_path = input("Enter your path: ")
age = 1
if not os.path.exists(req_path):
    print("Please provide valid path: ")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide directory path: ")
    sys.exit(2)
today = datetime.datetime.now()
print(f"Today date is: {today}")
for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path, each_file)
    if os.path.isfile(each_file_path):
        file_creating_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        difference_days = (today-file_creating_date).days
        if difference_days > age:
            print(each_file_path, "Days: ", (today-file_creating_date).days)
            dir(os).remove()
