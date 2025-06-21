# Import the picle module
import pickle

# Our data
customer_names = ["Jim Smith", "Amber Dobson", "Al James"]

# Write to disk
with open("customers.dat", mode = "wb") as f:
    pickle.dump(customer_names, f)

# Load the data
with open("customers.dat", mode = "rb") as f:
    loaded_data = pickle.load(f)

print(f"Original Data: {customer_names}")
print(f"Loaded data: {loaded_data}")
