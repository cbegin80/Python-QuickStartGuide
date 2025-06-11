# Import datetime
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Create a delta of 18 hours and 49 minutes
delta = datetime.timedelta(hours = 18, minutes = 49)

# Subtract this delta and store in previous_time
previous_time = now - delta

# Display the time minus the delta
print(now)
print(previous_time)