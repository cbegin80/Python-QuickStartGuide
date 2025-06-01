# Import the regular expression engine
import re

# Define our content
text = "Hello, World!"

# Does the string end with an exclaimation point?
if re.search("\!$", text):
    print("The string ends with !.")
else:
    print("The string does not end with !.")