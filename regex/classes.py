import re

lyrics = """On the 12th day of Christmas my true love sent to me
12 Lords a leaping, 11 ladies dancing, 10 pipers piping
9 drummers drumming, 8 maids a milking
7 swans a swimming, 6 geese a laying
And 5 gold rings, 4 calling birds, 3 French hens, 2 turtle doves
And a partridge in a pear tree"""

xmasRegex = re.compile(r'\d+\s\w+')

print(xmasRegex.findall(lyrics))


# Make your own character class:
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall(lyrics))

doubleVowelREgex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelREgex.findall(lyrics))

notVowelRegex = re.compile(r'[^aeiouAEIOU]')
print(notVowelRegex.findall(lyrics))
