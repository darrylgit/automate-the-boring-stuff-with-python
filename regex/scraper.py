import re
import pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)      # first separator
\d\d\d      # first 3 digits
-           # separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x) # extention word-part (optional)
(\d{2,5}))?
)       # extension number-part (optional)
''', re.VERBOSE)

# Create a regex for email address
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract email/phone from this text
extractedPhoneNumbers = phoneRegex.findall(text)
extractedEmailAddresses = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhoneNumbers:
    allPhoneNumbers.append(phoneNumber[0])


# Copy extracted data to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + \
    '\n'.join(extractedEmailAddresses)

pyperclip.copy(results)
