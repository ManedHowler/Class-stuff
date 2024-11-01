# Reads the allowed vehicles file into a list
def load_vehicles_from_file():
    try:
        with open('allowed_vehicles.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If file doesn't exist, return empty list
        return []

# Writes list of allowed vehicles to the file
def save_vehicles_to_file():
    with open('allowed_vehicles.txt', 'w') as file:
        for vehicle in AllowedVehiclesList:
            file.write(vehicle + '\n')

# List that will hold the allowed vehicles, loaded from file at startup
AllowedVehiclesList = load_vehicles_from_file()

# Displays menu to user
def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

# Displays list of authorized vehicles
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Search for the vehicle on the Allowed list
def search_vehicle():
    vehicle_name = input("\nPlease Enter the full Vehicle name: ")
    if vehicle_name in AllowedVehiclesList:
        print(f"\n{vehicle_name} is an authorized vehicle")
    else:
        print(f"\n{vehicle_name} is not an authorized vehicle, please check the spelling and try again.")

# Adds a vehicle to the Allowed list and saves to file
def add_vehicle():
    vehicle_name = input("\nPlease Enter the full Vehicle name you would like to add: ")
    if vehicle_name not in AllowedVehiclesList:
        AllowedVehiclesList.append(vehicle_name)
        save_vehicles_to_file()
        print(f'\nYou have added "{vehicle_name}" as an authorized vehicle')
    else:
        print(f'\n"{vehicle_name}" is already an authorized vehicle.')

# Deletes vehicle from the Allowed list and saves to file
def delete_vehicle():
    vehicle_name = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ")
    if vehicle_name in AllowedVehiclesList:
        confirmation = input(f'Are you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? (yes/no): ').lower()
        if confirmation == 'yes':
            AllowedVehiclesList.remove(vehicle_name)
            save_vehicles_to_file()
            print(f'\nYou have REMOVED "{vehicle_name}" as an authorized vehicle')
        else:
            print(f'\n"{vehicle_name}" was not removed.')
    else:
        print(f'\n"{vehicle_name}" is not an authorized vehicle.')

# Function that handles menu choice
def handle_menu_choice(choice):
    if choice == '1':
        print_vehicles()
    elif choice == '2':
        search_vehicle()
    elif choice == '3':
        add_vehicle()
    elif choice == '4':
        delete_vehicle()
    elif choice == '5':
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        return False  # Exits the main loop
    else:
        print("\nPlease select option 1, 2, 3, 4, or 5.")
    return True  # Continues the main loop

# Executes main function
def main():
    while True:
        print_menu()
        choice = input("\nEnter choice: ")
        if not handle_menu_choice(choice):
            break

if __name__ == "__main__":
    main()
