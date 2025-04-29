# Divide a number by zero

a = 7
b = 0

try:
    print(f"{a} divided by {b} is {a / b}")
except ZeroDivisionError as e:
    print("Sorry, a problem occurred dividing the numbers.")
    print(f"Error details: {e}")


print("All done!")