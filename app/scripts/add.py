import uuid
from datetime import datetime
from random import random

from app.services.task_handler import save_tasks, load_tasks

def add(description):
    tasks = load_tasks()
    status = "to-do"
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {"id": task_id, "description": description, "status": status, "createdAt": created_at,
            "updatedAt": updated_at}
    tasks.append(task)
    save_tasks(tasks)
    print("Task created successfully")