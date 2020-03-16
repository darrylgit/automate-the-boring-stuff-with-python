import re

# ? (match preceding group zero or one times)
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batwoman')
print('Find Batman or Batwoman:', mo.group())


phoneNumRegexOptionalAreaCode = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo2 = phoneNumRegexOptionalAreaCode.search(
    "This phone number, 456-1234, has no area code.")
print("But that's fine, we can do without.", mo2.group())


# * (match zero or more)
rockyHorrorRegex = re.compile(r'antici(.)*( )*pation')
mo3 = rockyHorrorRegex.search("antici....... pation")
print("I see you shiver with", mo3.group())
mo4 = rockyHorrorRegex.search("Whatever, anticipation")
print("No shivers here:", mo4.group())

# + (match one or more)
hamburgersRegex = re.compile(r'(\d)+ hamburgers')
mo5 = hamburgersRegex.search('Gimme 100 hamburgers')
print('Order up:', mo5.group())

# {x} (match specific number of times)
ellipsesRegex = re.compile(r'(\.){3}')
print(ellipsesRegex.search("Idk man...").group())

# {x, y} (match a range of times)
longEllipsesRegex = re.compile(r'(\.){3,}')
print(longEllipsesRegex.search("Idk bro........").group())

# Greedy and non-greedy matches
greedyMoo = re.compile(r'M(o){2,10}')
nongreedyMoo = re.compile(r'M(o){2,10}?')
moo = "Mooooooo"
print("Greedy match:", greedyMoo.search(moo).group())
print("Non-greedy match:", nongreedyMoo.search(moo).group())
