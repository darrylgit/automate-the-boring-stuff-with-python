import shutil
import os

os.chdir('/home/daniel/Coding/automate-the-boring-stuff/files')
# os.makedirs(os.getcwd() + '/dest')

# shutil.copy('deadhead.txt', './dest')

# shutil.copytree("./dest", "./dest-backup")

# Rename a file by "moving" it to the folder it's already in and giving it a new name
shutil.move('./dest-backup/deadhead.txt', './dest-backup/deadhead-backup.txt')
