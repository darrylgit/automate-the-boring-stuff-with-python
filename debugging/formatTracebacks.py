import traceback
import os

os.chdir('/home/daniel/Coding/automate-the-boring-stuff/debugging')

try:
    raise Exception("This is the error message")
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc() + "\n")
    errorFile.close()
    print('The traceback info was written to error_log.txt')
