from app.menus.mark_task_menu import mark_task_menu
from app.scripts.list_tasks import list_all_tasks
import sys
from app.menus.task_manager_menu import task_manager_menu

def initial_menu():
    menu_options = {
        "1": "Add, Update, and Delete tasks",
        "2": "Mark a task as in progress or done",
        "3": "List all tasks",
        "4": "List all tasks that are done",
        "5": "List all tasks that are not done",
        "6": "List all tasks that are in progress",
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
        task_manager_menu()
    elif choice == "2":
        mark_task_menu()
    elif choice == "3":
        list_all_tasks()
    # elif choice == "4":
    #     list_done_tasks()
    # elif choice == "5":
    #     list_not_done_tasks()
    # elif choice == "6":
    #     list_in_progress_tasks()
    else:
        print("Invalid option. Please try again.")
        initial_menu()
    input("\nPress Enter to return to the menu.")
    initial_menu()