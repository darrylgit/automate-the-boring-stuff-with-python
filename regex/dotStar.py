import re


# ^ (beginning pattern)
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search("Hello there!"))


# $ (ending pattern)
endsWithWorldRegex = re.compile(r'world$')
print(endsWithWorldRegex.search('Hello, world'))


# Combine to match an entire string
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('234234'))


# . (wildcard: any character except newline)
atRegex = re.compile(r'.at')
print(atRegex.findall('The hat on the mat'))

# .* (match whatever)
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall("First Name: Daniel Last Name: Wagener"))

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall('<To serve humans> for dinner>'))

# re.DOTALL (makes the wildcard match newlines too)
hamlet = "To be or not to be, that is the question \n Whether tis nobler in the mind to suffer \n The slings and arrows of outrageous fortune \n Or to take arms against a sea of troubles \n And by opposing, end them."
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(hamlet).group())

# Case insensitivity
vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall(hamlet))
