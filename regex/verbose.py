import re

re.compile(r'''
\d\d\d      # Woah, you can add comments inside the regex!
-
\d\d\d
-
\d\d\d\d''', re.VERBOSE)


# Pass multiple options using the bitwise OR operator
re.compile(r'''
\d\d\d      # Woah, you can add comments inside the regex!
-
\d\d\d
-
\d\d\d\d''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
