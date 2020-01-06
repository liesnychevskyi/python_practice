import os

# my_name = "Stanislav"
# my_new_name = "Billionaire"
# my_info = """I started my carrier as
# new ole-hadash
# and moved
# into Billionaire"""
# print(f"my name is: {my_name}\nmy new name: {my_new_name}\nmy info is: {my_info}")
# =====================================================================================================//
my_str_0 = ""
my_str_1 = " "
my_str_3 = 'Something'
print("my_str_0 is: ", bool(my_str_0))  # if is empty it is be false
print("my_str_1 is: ", bool(my_str_1))  # if is something in side the variable even space, it is be true
print("my_str_3 is: ", bool(my_str_3))  # if is something in side the variable even space, it is be true
indexing = "Python the best for automation"
print(indexing[0])
print(indexing[1])
print(indexing[2])
print(indexing[3])
print(indexing[4])
print(indexing[5])
print(indexing[6])
print(indexing[7])
print(indexing[8])
print(indexing[9])
print(indexing[10])
print(indexing[11])
print(indexing[12])
print(indexing[13])
print(indexing[14])
print(indexing[15])
print(indexing[16])
print(indexing[17])
print(indexing[18])
print(indexing[19])
print(indexing[20])
print(indexing[21])
print(indexing[22])
print(indexing[23])
print(indexing[24])
print(indexing[25])
print(indexing[26])
print(indexing[27])
print(indexing[28])
print(indexing[29])
print("||-------------------------------------------------------------------------------------||")
print(indexing[-1])  # -1 - prints the last index (character) of the string
print("||-------------------------------------------------------------------------------------||")
part_of = indexing[0:6]  # we can store part of sentence  into variable
print("Part of sentence: ", part_of)  # [0:6] - it means printing from 0 index to 6
print("||-------------------------------------------------------------------------------------||")

print(indexing[0:])  # [0:] - it means printing from 0 index to the end

print("||-------------------------------------------------------------------------------------||")

# ==================================== delete =================================================================//
del my_str_0    # deleting string
# print(my_str_0) # we cant use str after deleting
print("||---------------------- length ---------------------------------------------------------------||")
print("Length of INDEXING string is:", len(indexing))
print(f'Length of INDEXING string is: {len(indexing)}')

print("||----------------------------- concatenation two str --------------------------------------------------------||")
one = "Stas"
two = "Billionaire"
space = " "
my_future = one + space + two
print(my_future)
print(one + space + two)
print("||------------------------ case conversions string operation -------------------------------------------------||")
str_0 = "stas"
str_1 = "liesnychevskyi"
str_2 = "billionaire"
future = str_0.capitalize() + space + str_2.capitalize()
print(future)
print(future.upper())
print("||------------------------- dir - all available functions of string ------------------------------------------||")
print(dir(str_0))
print("||----------------------------- title function --------------------------------------------------------||")
print(my_future.title())
print("||----------------------------- input function --------------------------------------------------------||")
input_str = input("Enter string here: ")
print(input_str)
print(input_str.center(122))
print(input_str.ljust(122))
print(input_str.rjust(122))

print("||-----------------------------  os get terminal size --------------------------------------------------------||")

print("||-----------------------------  function --------------------------------------------------------||")
print("||-----------------------------  function --------------------------------------------------------||")
print("||-----------------------------  function --------------------------------------------------------||")
print("||-----------------------------  function --------------------------------------------------------||")
print("||-----------------------------  function --------------------------------------------------------||")
print("||-----------------------------  function --------------------------------------------------------||")


