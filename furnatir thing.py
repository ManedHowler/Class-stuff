# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Calculate profit as retail price minus wholesale price
profit = retailPrice - wholesalePrice

# Calculate sale price with 25% discount
discount_rate = 0.25
salePrice = retailPrice * (1 - discount_rate)

# Calculate profit when sale price is used
saleProfit = salePrice - wholesalePrice

# Print the results
print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(format(salePrice, ".2f")))  # Format salePrice to 2 decimal places
print("Sale Profit: $" + str(format(saleProfit, ".2f")))  # Format saleProfit to 2 decimal places