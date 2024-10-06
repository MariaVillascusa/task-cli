from datetime import datetime

from app.services.task_handler import load_tasks, save_tasks


def mark_as_in_progress(task_to_mark):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_to_mark:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Task marked as in-progress")
            break
    else:
        print("Task not found")
        return
    save_tasks(tasks)
