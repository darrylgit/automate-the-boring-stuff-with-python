import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

resume = "My home phone is 123-123-1234, my cell phone is 345-345-3456, and my reference's phone is 567-567-5678. Hire me plz"

print(phoneNumRegex.findall(resume))

# If the regex has two or more groups, the return is a list of tuples
phoneNumRegexWithGroups = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

print("Behold the tuples:", phoneNumRegexWithGroups.findall(resume))
