f = open('2-Inputs.py')  # Opening a File
f.close()  # closing a File

# f.read()
#  --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
#     ========= ===============================================================
#
# #     'r'       open for reading (default)
# with open('2-Inputs.py', 'r') as f:  # Open and close a file
#     # f.seek(0)
#     read = f.read()
    # print(type(read))

#     'x'       create a new file and open it for writing
# with open('myfile.txt', 'x') as myfile:
#     # can not perform read operations
#     myfile.write('My File')
#
#     'w'       open for writing, truncating the file first
# with open('myfile.txt', 'w') as myfile:
#     myfile.write('Tech Amplifiers')


#     'a'       open for writing, appending to the end of the file if it exists
# with open('myfile.txt', 'a') as myfile:
#     myfile.write(' Mukund ')

#     'b'       binary mode
# with open('myfile.txt', 'rb') as myfile:
#     print(myfile.read())

#     '+'       open a disk file for updating (reading and writing)
# with open('myfile.txt', '+a') as myfile:
#
#     myfile.write(' Mukundaa 123 ')
#     myfile.seek(0)
#
#     print(myfile.read())


# with open('myfile.txt', '+a') as myfile:
#     myfile.seek(0)  # move my cursor to perticular position
#     # print(myfile.read(10))
#     myfile.truncate()
    # print(myfile.tell())    # index of my cursor
    # myfile.seek(0)
    # print(myfile.readline())    # a single line
    # print(myfile.readline())
    # for i in myfile:
    #     print('new line ')
    #     print(i)          # single lines
    # myfile.seek(0)
    # print(myfile.readlines())


# Delete a file

# import os
#
# if os.path.exists("__init__.py"):
#     os.remove("__init__.py")
#     print("File deleted !")
# else:
#     print("File does not exist !")



# Rename a file

# import os
# #
# if os.path.exists("D:\\1 - TechAmplifiers\Demo"):
#     os.rename("D:\\1 - TechAmplifiers\Demo", "D:\\1 - TechAmplifiers\DEMO")
#     print("File Renamed !")
# else:
#     print("File does not exist !")