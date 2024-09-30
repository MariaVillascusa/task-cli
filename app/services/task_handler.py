import json
import os

FILENAME = 'data.json'
TASKS_JSON_PATH = os.path.join(os.path.dirname(__file__), '../data', FILENAME)

def load_tasks():
    if not os.path.exists(TASKS_JSON_PATH):
        return []

    with open(TASKS_JSON_PATH, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(TASKS_JSON_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

