# Import the regular expression engine
import re

# Define our content
text = "Hello, World!"

# Is "Hello" in our string?
if re.search("hello", text, re.IGNORECASE):
    print("Hello is in the string.")
else:
    print("Hello is not in the string.")