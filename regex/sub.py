import re

namesRegex = re.compile(r'Agent \w+')

print(namesRegex.sub(
    'REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

# Sub only part of the agents' names
namesRegex2 = re.compile(r'Agent (\w)\w+')
# Here, 1 referes to group 1 defined above
print(namesRegex2.sub(r'Agent \1*****',
                      'Agent Alice gave the secret documents to Agent Bob.'))
