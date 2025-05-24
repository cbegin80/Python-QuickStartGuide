# Define a new class
class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def greet(self):
        print(f"Hello, {self.name}!")

# Create three objects based on the customer class
c1 = Customer("Sarah", "Atlanta")
c2 = Customer("Robert", "Florence")
c3 = Customer("Thomas", "Denver")

# Add the customer objects to a list
customers = [c1, c2, c3]

# Iterate through the list, greet, then display information
for c in customers:
    c.greet()
    print(f"{c.name} lives in {c.city}.")