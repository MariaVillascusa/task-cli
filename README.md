# Task CLI

This is a simple Command Line Interface (CLI) application for tracking and managing your tasks. It allows users to add, update, delete, and manage tasks in a JSON file. The tasks can be marked as "to do," "in progress," or "done." This application is designed to help users practice basic programming concepts, work with the filesystem, handle user input, and build a simple CLI tool.

## Features

* Add tasks with descriptions
* Update and delete tasks
* Mark tasks as "in progress" or "done"
* List tasks by status:
* All tasks
* Tasks that are done
* Tasks that are in progress
* Tasks that are still to do (not done)


## Installation

The application can be installed as a Python package using pip:

`pip install .`

Once installed, you can access the task-cli command from your terminal.

## Usage

The application accepts commands and arguments through the command line. Below is a list of available commands and their usage:

### Add a New Task

Add a new task by providing a description:

`task-cli add "Buy groceries"`


### Update a Task

Update a task's description by providing the task ID and the new description:

`task-cli update <task_id> "Buy groceries and cook dinner"`

### Delete a Task
Delete a task by providing its ID:

`task-cli delete <task_id>
`
### Mark a Task as In Progress or Done

Mark a task as "in progress" by specifying its ID:

`task-cli mark-in-progress <task_id>`

Mark a task as "done" by specifying its ID:

`task-cli mark-done <task_id>`

### List All Tasks
To list all tasks, use the following command:

`task-cli list`

### List Tasks by Status

You can filter tasks based on their status: done, todo, or in-progress.

List all completed tasks:

`task-cli list done`

List all tasks that are still to do:

`task-cli list todo`

List all tasks that are currently in progress:

`task-cli list in-progress`

## Task Properties

Each task in the system has the following properties:

* id: A unique identifier for the task
* description: A short description of the task
* status: The status of the task (todo, in-progress, or done)
* createdAt: The date and time when the task was created
* updatedAt: The date and time when the task was last updated

These properties are saved in the data.json file in the current directory.

## Storage

The tasks are stored in a JSON file located in the current directory. If the file does not exist, it will be created automatically when you add a task.


## License
This project is released under the MIT License.

