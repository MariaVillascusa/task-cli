import os
import pytest

from app.scripts.add import add
from app.scripts.delete import delete
from app.services.task_handler import load_tasks

def test_add():
    tasks = load_tasks()
    assert len(tasks) == 0

    add('Task 1')
    tasks = load_tasks()
    assert len(tasks) == 1
    task = tasks[0]
    assert task['id'] == 1
    assert task['description'] == 'Task 1'
    assert task['status'] == 'to-do'
    delete(1)

if __name__ == '__main__':
    pytest.main()
