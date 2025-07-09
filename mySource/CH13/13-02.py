# Import urlopen from the urllib module
from urllib.request import urlopen

# Import regular expression functionality
import re

# Import unescape from HTML
from html import unescape

# URL to GET
url = "https://en.wikipedia.org/w/api.php?action=parse&prop=wikitext&format=json&page=Mount_Tambora"

# Request the page
response = urlopen(url)

# Get the page content
page_content = str(response.read())

# Unescape the page
page_content = unescape(page_content)

# Use this expression to find the elevation of Mt. Tambora
regex = r"elevation\_m\s=\s(\d*)"

result = []
# Perform the search
result = re.search(regex, page_content)

# Fetch the second element of the match (which is the elevation)
elevation = result[1]

# Print the elevation
print(f"The elevation of Mt. Tambora is {elevation}.")