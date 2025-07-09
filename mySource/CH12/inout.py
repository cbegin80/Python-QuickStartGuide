# Import sys module
import sys

# Read stfin into data_in
data_in = sys.stdin.read()

# Write to stdout
bytes_written = sys.stdout.write(data_in)

# Display stats
print(f"Wrote {bytes_written}")