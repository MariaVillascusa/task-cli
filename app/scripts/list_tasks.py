from app.services.task_handler import load_tasks

def list_all_tasks():
    tasks = load_tasks()
    print(tasks)
    print("All tasks:")
    for task in tasks:
        print(f'{task["status"]}: {task["description"]}')

