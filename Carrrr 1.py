# List of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Displays menu to user
def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

# Displays list of authorized vehicles
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Gives choice prompt
def main():
    while True:
        print_menu()
        choice = input("\nEnter choice: ")
        
        # Choices for prompt
        if choice == '1':
            print_vehicles()
        elif choice == '2':
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nPlease select option 1 or 2.")
# Executes main function
if __name__ == "__main__":
    main()
