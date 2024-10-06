from app.services.task_handler import load_tasks


def list_in_progress():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "in-progress":
            print(f'{task["id"]}. {task["status"]}: {task["description"]}')