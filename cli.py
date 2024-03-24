import sys
from .models import Location, Property, Tenant
from .database import Session, create_database

def main_menu():
    while True:
        print("1. Locations")
        print("2. Properties")
        print("3. Tenants")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            location_menu()
        elif choice == '2':
            property_menu()
        elif choice == '3':
            tenant_menu()
        elif choice == '4':
            sys.exit()

def location_menu():
    while True:
        print("1. Add a new location")
        print("2. Show property location")
        print("3. Back to main menu")
        choice = input("Select an option: ")
        if choice == '1':
            add_location()
        elif choice == '2':
            show_property_location()
        elif choice == '3':
            break

def add_location():
    session = Session()
    name = input("Enter location name: ")
    location = Location(name=name)
    session.add(location)
    session.commit()
    print(f"Location '{name}' added successfully")

def show_property_location():
    session = Session()
    properties = session.query(Property).all()
    for prop in properties:
        print(f"{prop.name} is located in {prop.location.name}")

def property_menu():
    pass  # Implement property menu operations

def tenant_menu():
    pass  # Implement tenant menu operations

if __name__ == "__main__":
    create_database()
    main_menu()
