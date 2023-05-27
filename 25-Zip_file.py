from zipfile import ZipFile
import zipfile

# with ZipFile('myzip.zip', 'a') as z:
#     z.write('3-somethings.py')
#     print(z.read('2-Inputs.py'))


with zipfile.ZipFile('E:\myzip.zip', 'r') as z:
    # print(z.namelist())
    # z.write('2-Inputs.py')
    # z.write('3-somethings.py')
    z.extractall()
    z.extract('3-somethings.py')


# write a script to create a backup into a zipfile of current directory after running the script