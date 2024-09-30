import uuid
from datetime import datetime
from app.services.task_handler import save_tasks, load_tasks

def create():
    tasks = load_tasks()
    print("Create a task")
    description = input("Enter the task description: ")
    status = "to-do"
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_id = str(uuid.uuid4())
    task = {"id": task_id, "description": description, "status": status, "createdAt": created_at,
            "updatedAt": updated_at}
    print(task)
    tasks.append(task)
    save_tasks(tasks)
    print("Task created successfully")