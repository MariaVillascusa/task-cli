from datetime import datetime

from app.services.task_handler import load_tasks, save_tasks


def update(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Task marked as done")
            break
    else:
        print("Task not found")
        return
    save_tasks(tasks)
