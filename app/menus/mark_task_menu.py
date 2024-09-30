import sys

from app.scripts.mark_as_done import mark_as_done
from app.scripts.mark_as_in_progress import mark_as_in_progress


def mark_task_menu():
    menu_options = {
        "1": "Mark as in progress",
        "2": "Mark as done",
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
        mark_as_in_progress()
    elif choice == "2":
        mark_as_done()
    else:
        print("Invalid option. Please try again.")
        mark_task_menu()