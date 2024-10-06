from app.services.task_handler import load_tasks, save_tasks


def delete(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted")
            break
    else:
        print("Task not found")
        return
    save_tasks(tasks)
