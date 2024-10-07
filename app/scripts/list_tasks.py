from app.services.task_handler import load_tasks

def list_all_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks')
        return
    for task in tasks:
        print(f'{task["id"]}. {task["status"]}: {task["description"]}')

