from rental_management_system.models.location import Location
from rental_management_system.models.property import Property
from rental_management_system.models.tenant import Tenant
from rental_management_system.database import SessionLocal, engine
from rental_management_system.utils import clear_screen

def main_menu():
    while True:
        clear_screen()
        print("Rental Management System")
        print("------------------------")
        print("1. Manage Locations")
        print("2. Manage Properties")
        print("3. Manage Tenants")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            location_menu()
        elif choice == "2":
            property_menu()
        elif choice == "3":
            tenant_menu()
        elif choice == "4":
            break
        else:
            input("Invalid choice. Press Enter to continue...")

def location_menu():
    while True:
        clear_screen()
        print("Location Menu")
        print("-------------")
        print("1. Add Location")
        print("2. Show Locations")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_location()
        elif choice == "2":
            show_locations()
        elif choice == "3":
            break
        else:
            input("Invalid choice. Press Enter to continue...")

def add_location():
    name = input("Enter location name: ")
    location = Location(name=name)

    with SessionLocal() as session:
        session.add(location)
        session.commit()
        print("Location added successfully.")

def show_locations():
    with SessionLocal() as session:
        locations = session.query(Location).all()

        if not locations:
            print("No locations found.")
        else:
            for location in locations:
                print(f"{location.id}. {location.name}")

        input("Press Enter to continue...")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    main_menu()
