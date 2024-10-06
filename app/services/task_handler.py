import importlib.resources
import json
import os
from config import get_json_file_path

#package execution
with importlib.resources.path('app.data', get_json_file_path()) as json_path:
    TASKS_JSON_PATH = str(json_path)

#local execution
# main_directory = os.path.dirname(os.path.abspath(__file__ + "/.."))
# FILENAME = 'data.json'
# TASKS_JSON_PATH = os.path.join(main_directory, 'data', FILENAME)



def load_tasks():
    if not os.path.exists(TASKS_JSON_PATH):
        return []
    with open(TASKS_JSON_PATH, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks, is_test=False):
    with open(TASKS_JSON_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

