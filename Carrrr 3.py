# List of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Displays menu to user
def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.3")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")

# Displays list of authorized vehicles
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Search for the vehicle on Allowed list
def search_vehicle():
    vehicle_name = input("\nPlease Enter the full Vehicle name: ")
    if vehicle_name in AllowedVehiclesList:
        print(f"\n{vehicle_name} is an authorized vehicle")
    else:
        print(f"\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")

# Adds a vehicle to the Allowed list
def add_vehicle():
    vehicle_name = input("\nPlease Enter the full Vehicle name you would like to add: ")
    if vehicle_name not in AllowedVehiclesList:
        AllowedVehiclesList.append(vehicle_name)
        print(f'\nYou have added "{vehicle_name}" as an authorized vehicle')
    else:
        print(f'\n"{vehicle_name}" is already an authorized vehicle.')

# Function that handles menu choice
def main():
    while True:
        print_menu()
        choice = input("\nEnter choice: ")
        
        # Choices for prompt
        if choice == '1':
            print_vehicles()
        elif choice == '2':
            search_vehicle()
        elif choice == '3':
            add_vehicle()
        elif choice == '4':
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nPlease select option 1, 2, 3, or 4.")
            
# Executes main function
if __name__ == "__main__":
    main()
