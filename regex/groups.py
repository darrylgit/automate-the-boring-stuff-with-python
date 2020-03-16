import re

message = "Call me 123-123-1234 because that's totes a real phone number."

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search(message)

# Not zero indexed wtf
print("The area code is %s and the rest of the phone number is %s" %
      (mo.group(1), mo.group(2)))

# Escaping parentheses
message2 = "Call me (123) 123-1234 because that's totes a real phone number."

parenthesesPhoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo2 = parenthesesPhoneNumRegex.search(message2)

print('Look ma, escaped parentheses: %s' % (mo2.group()))

# Pipe Character
batRegex = re.compile(r'Bat(mobile|copter|man|bat)')
mo3 = batRegex.search(r"Let's get in the Batmobile")

print("Today's bat-word is: %s" % (mo3.group()))
