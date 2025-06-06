# Import the regular expression engine
import re

# Our string
test = "The quick brown fox is fast!"

# Substitute spaces with +
plus_text = re.sub("\s+", "+", test)
print(plus_text)