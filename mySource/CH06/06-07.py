# Define a new class
class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __enter__(self):
        print("Entering scope.")
        # Run code upon entering the scope of the with statement
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving scope.")
        # Run code upon leaving the scope of the with statement

    def greet(self):
        print(f"Hello, {self.name}!")

# Use with to create a scope
with Customer("Robert", "Florence") as robert:
    robert.greet()