##fd = open("abc.txt")
##data = fd.read()
##print(data)

import os

fd = open("new_file_1.txt",'a')
fd.write("Hi vipul HOW are you?")
fd = open("new_file_1.txt")
data = fd.read()


print(data)
