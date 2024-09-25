# Input data
employee_name = input("Enter the employee's name: ")
total_transaction_value = float(input("Enter the total dollar value of transactions: "))
number_of_transactions = int(input("Enter the number of transactions: "))
shifts_worked = int(input("Enter the number of shifts worked: "))

# calculate productivity bonus
def calculate_bonus(employee_name, total_transaction_value, number_of_transactions, shifts_worked):

    productivity_score = (total_transaction_value / number_of_transactions) / shifts_worked

    # Determine bonus with nested if statement
    if productivity_score <= 30:
        bonus = 50.00
    else:
        if productivity_score <= 69:
            bonus = 75.00
        else:
            if productivity_score <= 199:
                bonus = 100.00
            else:
                bonus = 200.00
    
    # Print the employee's name and bonus
    print(f"Employee: {employee_name}")
    print(f"Bonus: ${bonus:.1f}")

# Calculate and display
calculate_bonus(employee_name, total_transaction_value, number_of_transactions, shifts_worked)
