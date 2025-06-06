# Ask the user for a value
value = input("Please enter a value: ")

# Check if every character is a number
# "3102" - True
# "4111123412341234" - True
# "04/22/2022" - False
# "1600 Pennsylvania Avenue" - False
if value.isnumeric():
    print("It's a number.")

# Check if every character is a letter
# Spaces, numbers, and punctuation don't count
# "Yes" - True
# "Yes " - False
# "Yes 3" - False
# "Yes!" - False
if value.isalpha():
    print("It's filled with alphabet characters only!")

# Check if the string is alphanumeric
# "1600 Pennsylvanie Avenue" - False
# "Washington DC" - False
# "Washington" - True
if value.isalnum():
    print("It's alphanumeric.")