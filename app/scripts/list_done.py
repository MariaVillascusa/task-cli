from app.services.task_handler import load_tasks


def list_done():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "done":
            print(f'{task["id"]}. {task["status"]}: {task["description"]}')
