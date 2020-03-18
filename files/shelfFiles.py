import os
import shelve

os.chdir('/home/daniel/Coding/automate-the-boring-stuff/files')

shelfFile = shelve.open('catdata')
# shelfFile['cats'] = ['Emma', 'Byron']
print(shelfFile['cats'])
shelfFile.close()
