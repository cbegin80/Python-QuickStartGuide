# Import datetime
import datetime

# Get the current time
now = datetime.datetime.now()

# Set the date to look forward to
goal_date = datetime.datetime(2025, 8, 17)

time_diff = goal_date - now

print(f"It is {time_diff.days} days til {goal_date.strftime('%B %d, %Y')}.")