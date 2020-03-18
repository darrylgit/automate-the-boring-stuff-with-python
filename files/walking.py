import os

os.chdir('/home/daniel/Coding/automate-the-boring-stuff/files')

for folderName, subfolders, filenames in os.walk('./walkMe'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in %s are: %s' % (folderName, str(filenames)))
    print()
