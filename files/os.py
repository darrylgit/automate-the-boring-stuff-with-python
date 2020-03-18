import os

lolFile = open('/home/daniel/lol.txt')

content = lolFile.read()
print(content)

lolFile.close()

# Write mode
# lolFile = open('/home/daniel/lol.txt', 'w')

# Appened mode
# lolFile = open('/home/daniel/lol.txt', 'a')

lmaoFile = open('/home/daniel/lmao.txt', 'w')
# lmaoFile.write('Ayyyyyyy lmao')
lmaoFile.close

print(os.getcwd())
os.chdir('/home/daniel/Coding/automate-the-boring-stuff/files')

roflFile = open('deadhead.txt', 'a')
roflFile.write("Hooray for you\n")
roflFile.close()
