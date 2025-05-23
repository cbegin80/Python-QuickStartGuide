# ClydeBank Coffee Shop Simulator 4000
# Copyright (C) 2023 ClydeBank Media, All Rights Reserved.

# Import items from the rnadom madule to generate weather
from random import seed, randint

# Current day number
day = 1

# Starting cash on hand
cash = 100.00

# Coffee on hand (cups)
coffee = 100

# Sales list of dictionaries
# sales = [
#     {
#         "day": 1,
#         "coffee_inv": 100,
#         "advertising": "10",
#         "temp": 68,
#         "cups_sold": 16
#     },
#     {
#         "day": 2,
#         "coffee_inv": 84,
#         "advertising": "15",
#         "temp": 72,
#         "cups_sold": 20
#     },
#     {
#         "day": 3,
#         "coffee_inv": 64,
#         "advertising": "5",
#         "temp": 78,
#         "cups_sold": 10
#     }
# ]

# Create an empty sales list
sales = []

# Print welcome message
print("ClydeBank Coffee Shop Simulator 4000, Version 1.00")
print("Copyright (C) 2022 ClydeBank Media, All Rights Reserved\n")
print("Let's collect some information before we start the game.\n")

# Get name and shop name
# 1. Set name and shop_name to False
# 2. Use while not name and shop_name to continue to prompt for a non-empty string

name = False
while not name:
    name = input("What is your name? ")

shop_name = False
while not shop_name:
    shop_name = input("What do you want to name your coffee shop? ")

# We have what we need, so let's get started!

print("\nOK, let's get started. Have fun!")

# The main game loop
running = True
while running:
    # Display the day and a "fancy" text effect
    print(f"\n-----| Day + {day} @  {shop_name} |-----")

    # Generate a random temperature between 20 and 90
    # We'll consider seasons later on, but this is good enough for now
    temperature = randint(20, 90)

    # Display the cash and weather
    print(f"You have ${cash} cash and it's {temperature} degrees.")
    print(f"You have coffee on hand to make {coffee} cups.")

    # Get price of a cup of coffee
    cup_price = input("What do you want to charge per cup of coffee? ")

    # Get advertising budget
    print("\nYou can buy advertising to help promote sales.")
    advertising = input("How much advertising do you want to buy (0 for none)? ")

    # Convert advertising into a float
    # If it fails, assign it to 0
    try:
        advertising = float(advertising)
    except ValueError:
        advertising = 0

    # Deduct advertising from cash on hand
    cash -= advertising

    #TODO: Calculate today's performance
    #TODO: Display today's performance

    # Before we loop around, add a day
    day += 1