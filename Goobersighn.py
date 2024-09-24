"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables
charge = 0.00  # Initial charge for the sign

# Taking sign detail inputs
numChars = int(input("Enter the number of characters in the sign: "))  # Number of characters in the sign
color = input("Enter the color of the characters (black, white, or gold): ").lower()  # Color of the characters
woodType = input("Enter the type of wood (pine or oak): ").lower()  # Type of wood

# Minimum charge for signs
charge = 35.00

# If there's more than 5 characters, add $4 for each extra character
if numChars > 5:
    charge += (numChars - 5) * 4

# If the sign is made of oak, add $20.00
if woodType == "oak":
    charge += 20.00

# If the color is gold, add $15.00
if color == "gold":
    charge += 15.00

# Output the total charge for this sign
print("The charge for this sign is $" + str(charge))
