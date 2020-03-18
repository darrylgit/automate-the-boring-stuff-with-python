import os
import shutil
import send2trash


os.chdir('/home/daniel/Coding/automate-the-boring-stuff/files')

# os.rmdir('./asdf')

# shutil.rmtree('./asdf')

send2trash.send2trash('./trashMe.txt')
