import os
import sys

# Add the project's root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the module
from rental_management_system.cli import main_menu

if __name__ == "__main__":
    main_menu()
