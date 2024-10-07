import pytest

from app.scripts.add import add
from app.scripts.delete import delete
from app.scripts.list_done import list_done
from app.scripts.list_in_progress import list_in_progress
from app.scripts.list_tasks import list_all_tasks
from app.scripts.list_todo import list_todo
from app.scripts.mark_as_done import mark_as_done
from app.scripts.mark_as_in_progress import mark_as_in_progress
from app.scripts.update import update
from app.services.task_handler import load_tasks


def test_add_and_delete():
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

def test_delete_non_existing_task(capsys):
    tasks = load_tasks()
    assert len(tasks) == 0
    delete(1)
    captured = capsys.readouterr()
    assert "Task not found" in captured.out

def test_update_task():
    add('Task 1')
    tasks = load_tasks()
    assert len(tasks) == 1
    update(1, 'updated task')
    tasks = load_tasks()
    assert len(tasks) == 1
    task = tasks[0]
    assert task['id'] == 1
    assert task['description'] == 'updated task'
    delete(1)

def test_update_non_existing_task(capsys):
    update(1, 'updated task')
    captured = capsys.readouterr()
    assert "Task not found" in captured.out

def test_list_all(capsys):
    add('Task 1')
    add('Task 2')
    mark_as_in_progress(2)
    list_all_tasks()
    captured = capsys.readouterr()
    assert "1. to-do: Task 1" in captured.out
    assert "2. in-progress: Task 2" in captured.out
    delete(1)
    delete(2)

def test_list_empty(capsys):
    list_all_tasks()
    captured = capsys.readouterr()
    assert "No tasks" in captured.out

def test_mark_as_done_and_list(capsys):
    add('Task 1')
    add('Task 2')
    mark_as_done(1)
    list_done()
    captured = capsys.readouterr()
    assert "1. done: Task 1" in captured.out
    assert "2. to-do: Task 2" not in captured.out
    delete(1)
    delete(2)

def test_mark_as_done_non_existing_task(capsys):
    mark_as_done(1)
    captured = capsys.readouterr()
    assert "Task not found" in captured.out

def test_mark_as_in_progress_and_list(capsys):
    add('Task 1')
    add('Task 2')
    mark_as_in_progress(1)
    list_in_progress()
    captured = capsys.readouterr()
    assert "1. in-progress: Task 1" in captured.out
    assert "2. to-do: Task 2" not in captured.out
    delete(1)
    delete(2)

def test_mark_as_in_progress_non_existing_task(capsys):
    mark_as_in_progress(1)
    captured = capsys.readouterr()
    assert "Task not found" in captured.out

def test_list_to_do(capsys):
    add('Task 1')
    add('Task 2')
    mark_as_done(1)
    list_todo()
    captured = capsys.readouterr()
    assert "2. to-do: Task 2" in captured.out
    assert "1. done: Task 1" not in captured.out
    delete(1)
    delete(2)



if __name__ == '__main__':
    pytest.main()
