from app.services.task_handler import load_tasks


def list_todo():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "to-do":
            print(f'{task["id"]}. {task["status"]}: {task["description"]}')