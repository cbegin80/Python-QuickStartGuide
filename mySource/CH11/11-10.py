# Import datetime
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Display the date and time in a custome format
print(now.strftime("%A, %B %d, %Y at %I:%M:%S %p %Z"))