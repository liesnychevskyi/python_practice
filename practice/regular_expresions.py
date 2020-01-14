import re

#  regex
# my_str = "Python is simple and it easy !"
# print(my_str)
# k = my_str.split("is")
# print(k)
# kk = re.split("i[st]]", my_str)
# print(kk)
# -----------------------------------------------------------#
# text = "123 This is a python and it is easy to learn 456"
# my_pattern_0 = "i[st]"  # it will looking for or is or it
# my_pattern_1 = "is"
# my_pattern_2 = "[a-g]"  # it will looking from 'a' to 'g' sequence
# my_pattern_3 = "[Tan]"  # it wil looking for T or a or n
# my_pattern_4 = "\w"  # it means all characters till 'w'
# my_pattern_5 = "\w\w"  # it will be looking for couple characters
# my_pattern_6 = '\W'  # spaces and symbols
# my_pattern_7 = "\d"  # any digits (number)
# my_pattern_8 = "."  # any char (\.) - just dot identification
# my_pattern_9 = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d"  # it takes just dots in the string
# text_2 = "My ip server is 192.255.255.03"
#
# print(re.findall(my_pattern_9, text_2))  # this method looking all "is" in the current string
# print(len(re.findall(my_pattern_9, text_2)))

# =====================================================================================================||
my_string = "This is about python. Python is easy to learn and we have two major version: python2 and python3"
my_pattern = r'\bpython[23]?\b'  # [23]? - it means or 2 or 3 after python2 or python3
print(re.findall(my_pattern, my_string))
print(re.findall(my_pattern, my_string, flags=re.I))  # flags - to find capital letters
print(re.search(my_pattern, my_string))
print(re.split(my_pattern, my_string))
#  pattern object
pat_object = re.compile(my_pattern, flags=re.I)
print(pat_object)
print(pat_object.findall(my_string))
print(pat_object.search(my_string))

#  re.findall(my_pattern, my_string) ===> re.compile(my_pattern).findall(my_string)
