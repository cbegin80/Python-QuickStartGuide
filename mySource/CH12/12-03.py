# String to write
data = """The lazy red fox slept instead of jumping over a dog.
The lazy dog ignored the fox and slept as well."""

# Write the data
with open("fox2.txt", mode = "w", encoding = "utf-8") as f:
    f.write(data)

# Read the data
with open("fox2.txt", mode = "r", encoding = "utf-8") as f:
    read_data = f.readlines()

# Display the results
print(f"Original: {data}")
print(f"Read from disk: {read_data}")