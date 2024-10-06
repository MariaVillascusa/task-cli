import sys

from app.scripts.add import add
from app.scripts.delete import delete
from app.scripts.list_done import list_done
from app.scripts.list_in_progress import list_in_progress
from app.scripts.list_tasks import list_all_tasks
from app.scripts.list_todo import list_todo
from app.scripts.mark_as_done import mark_as_done
from app.scripts.mark_as_in_progress import mark_as_in_progress
from app.scripts.update import update


def main():
    try:
        args = sys.argv
        if len(args) == 1:
            print("No arguments provided")
            sys.exit()
        if args[1] == 'add':
            if len(args) < 3:
                print("No description provided")
                sys.exit()
            add(args[2])
        if args[1] == 'update':
            if len(args) < 3:
                print("No task id provided")
                sys.exit()
            if len(args) < 4:
                print("No description provided")
                sys.exit()
            update(int(args[2]), args[3])
        if args[1] == 'delete':
            if len(args) < 3:
                print("No task id provided")
                sys.exit()
            delete(int(args[2]))
        if args[1] == 'list':
            if len(args) > 2 and args[2] == 'done':
                list_done()
                sys.exit()
            if len(args) > 2 and args[2] == 'todo':
                list_todo()
                sys.exit()
            if len(args) > 2 and args[2] == 'in-progress':
                list_in_progress()
                sys.exit()
            list_all_tasks()
        if args[1] == 'mark-done':
            if len(args) < 3:
                print("No task id provided")
                sys.exit()
            mark_as_done(int(args[2]))
        if args[1] == 'mark-in-progress':
            if len(args) < 3:
                print("No task id provided")
                sys.exit()
            mark_as_in_progress(int(args[2]))
    except ValueError as e:
        print('Argument not valid')
        sys.exit()
    except Exception as e:
        print('An error occurred', e)
        sys.exit()
