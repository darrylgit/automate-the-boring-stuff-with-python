import re

message = "Call me 123-123-1234 because that's totes a real phone number. Otherwise, 432-432-4321"

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search(message)
print(mo.group())

print(phoneNumRegex.findall(message))
