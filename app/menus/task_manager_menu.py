import sys
from app.scripts.create import create

def task_manager_menu():
    menu_options = {
        "1": "Add",
        "2": "Update",
        "3": "Delete",
        "0": "Exit"
    }
    print('Options:')
    for key, value in menu_options.items():
        print(f'{key}: {value}')
    choice = input("Enter your option: ")
    if choice == "0":
        print("Exiting...")
        sys.exit()
    elif choice == "1":
        create()
    elif choice == "2":
        print("Update")
    elif choice == "3":
        print("Delete")
    else:
        print("Invalid option. Please try again.")
        task_manager_menu()